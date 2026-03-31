"""
FastAPI Application for Aircraft Predictive Maintenance
Production-ready API for real-time component failure predictions
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator
from typing import List, Dict, Any, Optional
import logging
from datetime import datetime
import traceback

from src.model import PredictiveMaintenanceModel

# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ============================================================================
# FASTAPI INITIALIZATION
# ============================================================================
app = FastAPI(
    title="🛩️ Aircraft Predictive Maintenance API",
    description="Real-time ML-powered system for predicting aircraft component failures",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc"  # ReDoc documentation
)

# ============================================================================
# CORS CONFIGURATION (Allow web frontend access)
# ============================================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# GLOBAL MODEL INSTANCE
# ============================================================================
try:
    # Don't pass relative paths - let model.py compute from script location
    model = PredictiveMaintenanceModel()
    logger.info("Model loaded successfully at startup")
except Exception as e:
    logger.error(f"Failed to load model at startup: {e}")
    model = None

# ============================================================================
# PYDANTIC MODELS (Request/Response schemas)
# ============================================================================

class AircraftComponent(BaseModel):
    """Schema for a single aircraft component measurement (12 required features)"""
    aircraft_id: str = Field(..., description="Unique aircraft identifier")
    component_id: str = Field(..., description="Component identifier")
    flight_cycles: float = Field(..., ge=0, description="Number of flight cycles")
    engine_hours: float = Field(..., ge=0, description="Engine operating hours")
    temperature_sensor_1: float = Field(..., description="Temperature sensor 1 reading (°C)")
    temperature_sensor_2: float = Field(..., description="Temperature sensor 2 reading (°C)")
    vibration_sensor: float = Field(..., ge=0, description="Vibration sensor reading (Hz)")
    pressure_sensor: float = Field(..., ge=0, description="Pressure sensor reading (PSI)")
    fault_code_count: int = Field(..., ge=0, description="Number of active fault codes")
    last_maintenance_cycles: float = Field(..., ge=0, description="Cycles since last maintenance")
    maintenance_log_flag: int = Field(..., description="Maintenance log indicator (0 or 1)")
    ambient_temperature: float = Field(..., description="Ambient temperature (°C)")
    humidity: float = Field(..., ge=0, le=100, description="Humidity percentage")
    failure_within_10_cycles: int = Field(..., description="Future failure indicator (0 or 1)")
    
    class Config:
        schema_extra = {
            "example": {
                "aircraft_id": "AC001",
                "component_id": "ENG_001",
                "flight_cycles": 150.0,
                "engine_hours": 125.5,
                "temperature_sensor_1": 85.3,
                "temperature_sensor_2": 92.1,
                "vibration_sensor": 0.85,
                "pressure_sensor": 102.3,
                "fault_code_count": 0,
                "last_maintenance_cycles": 45.0,
                "maintenance_log_flag": 0,
                "ambient_temperature": 25.0,
                "humidity": 60.0,
                "failure_within_10_cycles": 0
            }
        }


class PredictionResponse(BaseModel):
    """Schema for prediction response"""
    prediction: int = Field(..., description="0: No Failure, 1: Failure")
    prediction_label: str = Field(..., description="Human-readable prediction label")
    failure_probability: float = Field(..., ge=0, le=1, description="Probability of failure")
    no_failure_probability: float = Field(..., ge=0, le=1, description="Probability of no failure")
    confidence: float = Field(..., ge=0, le=100, description="Model confidence percentage")
    recommended_action: str = Field(..., description="Recommended maintenance action")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Prediction timestamp")


class SinglePredictionRequest(BaseModel):
    """Request schema for single prediction"""
    component: AircraftComponent = Field(..., description="Component data to predict")


class SinglePredictionResponse(BaseModel):
    """Response schema for single prediction"""
    status: str = Field(default="success", description="Request status")
    aircraft_id: str
    component_id: str
    prediction: PredictionResponse
    

class BatchPredictionRequest(BaseModel):
    """Request schema for batch predictions"""
    components: List[AircraftComponent] = Field(..., description="List of components to predict")


class BatchPredictionResponse(BaseModel):
    """Response schema for batch predictions"""
    status: str = Field(default="success", description="Request status")
    total_predictions: int = Field(..., description="Number of predictions made")
    failures_detected: int = Field(..., description="Number of failures predicted")
    predictions: List[Dict[str, Any]] = Field(..., description="List of predictions")


class ModelInfoResponse(BaseModel):
    """Response schema for model information"""
    status: str = Field(default="success")
    model_type: str
    number_of_features: int
    feature_names: List[str]
    model_performance: Dict[str, float]
    imbalance_handling: str
    scaling_method: str


# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.on_event("startup")
async def startup_event():
    """Startup event handler"""
    logger.info("🚀 Aircraft Maintenance Prediction API starting up...")
    if model is None:
        logger.error(" Model failed to load at startup!")
    else:
        logger.info(" Model ready for predictions")


@app.get("/", tags=["Health"])
async def root():
    """Root endpoint - API welcome message"""
    return {
        "message": " Aircraft Predictive Maintenance API",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs",
        "endpoints": {
            "health": "/health",
            "predict_single": "/predict",
            "predict_batch": "/predict_batch",
            "model_info": "/model_info"
        }
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    if model is None:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                          detail="Model not loaded")
    return {
        "status": "healthy ",
        "model_loaded": True,
        "timestamp": datetime.utcnow()
    }


@app.post("/predict", response_model=SinglePredictionResponse, tags=["Predictions"])
async def predict_single(request: SinglePredictionRequest):
    """
    Make a single component failure prediction
    
    **Example Request:**
    ```json
    {
      "component": {
        "aircraft_id": "AC001",
        "component_id": "ENG_001",
        "flight_cycles": 150.0,
        "engine_hours": 125.5,
        ...
      }
    }
    ```
    """
    try:
        if model is None:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                              detail=" Model not loaded")
        
        # Extract features from request
        features = request.component.dict(exclude_none=True)
        
        logger.info(f"🔮 Predicting for aircraft {request.component.aircraft_id}, component {request.component.component_id}")
        
        # Get prediction
        prediction = model.predict_single(features)
        
        return SinglePredictionResponse(
            status="success",
            aircraft_id=request.component.aircraft_id,
            component_id=request.component.component_id,
            prediction=PredictionResponse(
                prediction=prediction["prediction"],
                prediction_label=prediction["prediction_label"],
                failure_probability=prediction["failure_probability"],
                no_failure_probability=prediction["no_failure_probability"],
                confidence=prediction["confidence"],
                recommended_action=prediction["recommended_action"]
            )
        )
        
    except ValueError as e:
        logger.error(f" Validation error: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f" Prediction error: {traceback.format_exc()}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                          detail=f" Prediction failed: {str(e)}")


@app.post("/predict_batch", response_model=BatchPredictionResponse, tags=["Predictions"])
async def predict_batch(request: BatchPredictionRequest):
    """
    Make predictions for multiple components in batch
    
    **Usage:** Submit multiple aircraft components for efficient batch processing
    
    **Example Request:**
    ```json
    {
      "components": [
        {"aircraft_id": "AC001", "component_id": "ENG_001", ...},
        {"aircraft_id": "AC002", "component_id": "ENG_002", ...}
      ]
    }
    ```
    """
    try:
        if model is None:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                              detail=" Model not loaded")
        
        logger.info(f"🔮 Batch predicting {len(request.components)} components...")
        
        predictions = []
        failures_count = 0
        
        for component in request.components:
            features = component.dict(exclude_none=True)
            pred = model.predict_single(features)
            
            prediction_data = {
                "aircraft_id": component.aircraft_id,
                "component_id": component.component_id,
                "prediction": pred["prediction"],
                "failure_probability": pred["failure_probability"],
                "recommended_action": pred["recommended_action"]
            }
            
            predictions.append(prediction_data)
            
            if pred["prediction"] == 1:
                failures_count += 1
        
        logger.info(f" Batch prediction complete: {failures_count} failures detected")
        
        return BatchPredictionResponse(
            status="success",
            total_predictions=len(predictions),
            failures_detected=failures_count,
            predictions=predictions
        )
        
    except ValueError as e:
        logger.error(f" Validation error: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f" Batch prediction error: {traceback.format_exc()}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                          detail=f" Batch prediction failed: {str(e)}")


@app.get("/model_info", response_model=ModelInfoResponse, tags=["Info"])
async def get_model_info():
    """
    Get information about the loaded model
    
    Returns model architecture, performance metrics, and features
    """
    try:
        if model is None:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                              detail= "Model not loaded")
        
        info = model.get_model_info()
        
        return ModelInfoResponse(
            status="success",
            model_type=info["model_type"],
            number_of_features=info["number_of_features"],
            feature_names=info["feature_names"],
            model_performance=info["model_performance"],
            imbalance_handling=info["imbalance_handling"],
            scaling_method=info["scaling_method"]
        )
        
    except Exception as e:
        logger.error(f"❌ Error retrieving model info: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                          detail=str(e))


# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom HTTP exception handler"""
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": "error", "detail": exc.detail}
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """General exception handler"""
    logger.error(f"❌ Unhandled exception: {traceback.format_exc()}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"status": "error", "detail": "Internal server error"}
    )


# ============================================================================
# RUN COMMAND (for local testing)
# ============================================================================
if __name__ == "__main__":
    import uvicorn
    logger.info("🚀 Starting FastAPI server...")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
