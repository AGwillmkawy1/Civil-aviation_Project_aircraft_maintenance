"""
Client Script for Testing Aircraft Maintenance Prediction API
Demonstrates how to use the FastAPI endpoints
"""

import requests
import json
from typing import Dict, List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ============================================================================
# CONFIGURATION
# ============================================================================
API_BASE_URL = "http://localhost:8000"
API_TIMEOUT = 10  # seconds


class MaintenancePredictionClient:
    """Client for Aircraft Maintenance Prediction API"""
    
    def __init__(self, base_url: str = API_BASE_URL):
        """Initialize client with API base URL"""
        self.base_url = base_url
        logger.info(f"🔗 Initialized client for {base_url}")
    
    def health_check(self) -> Dict:
        """Check if API is healthy"""
        try:
            response = requests.get(f"{self.base_url}/health", timeout=API_TIMEOUT)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"❌ Health check failed: {e}")
            return {"status": "error", "detail": str(e)}
    
    def get_model_info(self) -> Dict:
        """Get model information"""
        try:
            response = requests.get(f"{self.base_url}/model_info", timeout=API_TIMEOUT)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"❌ Failed to get model info: {e}")
            return {"status": "error", "detail": str(e)}
    
    def predict_single(self, component_data: Dict) -> Dict:
        """Make a single prediction"""
        try:
            payload = {"component": component_data}
            response = requests.post(
                f"{self.base_url}/predict",
                json=payload,
                timeout=API_TIMEOUT
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"❌ Single prediction failed: {e}")
            return {"status": "error", "detail": str(e)}
    
    def predict_batch(self, components_list: List[Dict]) -> Dict:
        """Make batch predictions"""
        try:
            payload = {"components": components_list}
            response = requests.post(
                f"{self.base_url}/predict_batch",
                json=payload,
                timeout=API_TIMEOUT
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"❌ Batch prediction failed: {e}")
            return {"status": "error", "detail": str(e)}


# ============================================================================
# SAMPLE DATA
# ============================================================================

SAMPLE_COMPONENT_NORMAL = {
    "aircraft_id": "AC001",
    "component_id": "ENG_001",
    "flight_cycles": 150.0,
    "engine_hours": 125.5,
    "temperature_sensor_1": 75.0,
    "temperature_sensor_2": 82.0,
    "vibration_sensor": 0.35,
    "pressure_sensor": 98.0,
    "fault_code_count": 0,
    "last_maintenance_cycles": 45.0,
    "maintenance_log_flag": 0,
    "ambient_temperature": 25.0,
    "humidity": 60.0,
    "failure_within_10_cycles": 0,
}

SAMPLE_COMPONENT_FAILURE_RISK = {
    "aircraft_id": "AC002",
    "component_id": "ENG_002",
    "flight_cycles": 350.0,
    "engine_hours": 280.0,
    "temperature_sensor_1": 95.0,  # High temperature
    "temperature_sensor_2": 105.0,  # High temperature
    "vibration_sensor": 1.85,  # High vibration
    "pressure_sensor": 112.0,  # High pressure
    "fault_code_count": 3,  # Active faults
    "last_maintenance_cycles": 280.0,  # Long time since maintenance
    "maintenance_log_flag": 1,  # Maintenance log available
    "ambient_temperature": 35.0,
    "humidity": 85.0,
    "failure_within_10_cycles": 1,
}


# ============================================================================
# DEMO FUNCTIONS
# ============================================================================

def demo_health_check():
    """Demo: Check API health"""
    print("\n" + "="*80)
    print("🔷 DEMO 1: Health Check")
    print("="*80)
    
    client = MaintenancePredictionClient()
    result = client.health_check()
    print(json.dumps(result, indent=2, default=str))


def demo_model_info():
    """Demo: Get model information"""
    print("\n" + "="*80)
    print("🔷 DEMO 2: Model Information")
    print("="*80)
    
    client = MaintenancePredictionClient()
    result = client.get_model_info()
    
    if result.get("status") == "success":
        print(f"Model Type: {result['model_type']}")
        print(f"Number of Features: {result['number_of_features']}")
        print(f"Performance Metrics:")
        for metric, value in result['model_performance'].items():
            print(f"  - {metric}: {value:.4f}")
        print(f"\nImbalance Handling: {result['imbalance_handling']}")
        print(f"Scaling Method: {result['scaling_method']}")
    else:
        print(json.dumps(result, indent=2))


def demo_single_prediction():
    """Demo: Make single predictions"""
    print("\n" + "="*80)
    print("🔷 DEMO 3: Single Predictions")
    print("="*80)
    
    client = MaintenancePredictionClient()
    
    # Test 1: Normal component
    print("\n📊 Test 1: Normal Operating Component")
    print("-" * 80)
    result = client.predict_single(SAMPLE_COMPONENT_NORMAL)
    if result.get("status") == "success":
        pred = result["prediction"]
        print(f"Aircraft: {result['aircraft_id']}")
        print(f"Component: {result['component_id']}")
        print(f"Prediction: {pred['prediction_label']}")
        print(f"Failure Probability: {pred['failure_probability']:.2%}")
        print(f"Confidence: {pred['confidence']:.2f}%")
        print(f"Action: {pred['recommended_action']}")
    else:
        print(json.dumps(result, indent=2))
    
    # Test 2: Component with failure risk
    print("\n Test 2: Component with Potential Failure Risk")
    print("-" * 80)
    result = client.predict_single(SAMPLE_COMPONENT_FAILURE_RISK)
    if result.get("status") == "success":
        pred = result["prediction"]
        print(f"Aircraft: {result['aircraft_id']}")
        print(f"Component: {result['component_id']}")
        print(f"Prediction: {pred['prediction_label']}")
        print(f"Failure Probability: {pred['failure_probability']:.2%}")
        print(f"Confidence: {pred['confidence']:.2f}%")
        print(f"Action: {pred['recommended_action']}")
    else:
        print(json.dumps(result, indent=2))


def demo_batch_prediction():
    """Demo: Make batch predictions"""
    print("\n" + "="*80)
    print("🔷 DEMO 4: Batch Predictions")
    print("="*80)
    
    client = MaintenancePredictionClient()
    
    # Create batch with multiple components
    batch_components = [
        SAMPLE_COMPONENT_NORMAL.copy(),
        SAMPLE_COMPONENT_FAILURE_RISK.copy(),
    ]
    
    # Add more variations
    component_3 = SAMPLE_COMPONENT_NORMAL.copy()
    component_3["aircraft_id"] = "AC003"
    component_3["component_id"] = "ENG_003"
    batch_components.append(component_3)
    
    result = client.predict_batch(batch_components)
    
    if result.get("status") == "success":
        print(f"\n✅ Batch Processing Complete!")
        print(f"Total Predictions: {result['total_predictions']}")
        print(f"Failures Detected: {result['failures_detected']} 🔴")
        print(f"\nDetailed Results:")
        print("-" * 80)
        for i, pred in enumerate(result['predictions'], 1):
            status = "🔴 FAILURE" if pred['prediction'] == 1 else "🟢 OK"
            print(f"{i}. {pred['aircraft_id']} / {pred['component_id']}: {status}")
            print(f"   Failure Prob: {pred['failure_probability']:.2%}")
            print(f"   Action: {pred['recommended_action'][:50]}...")
    else:
        print(json.dumps(result, indent=2))


# ============================================================================
# MAIN
# ============================================================================

def main():
    """Run all demos"""
    print("\n" + "="*80)
    print("🛩️  AIRCRAFT PREDICTIVE MAINTENANCE API - CLIENT DEMO")
    print("="*80)
    print("\nMake sure the FastAPI server is running:")
    print("  python src/main.py")
    print("or")
    print("  cd src && uvicorn main:app --reload")
    
    try:
        # Run demos
        demo_health_check()
        demo_model_info()
        demo_single_prediction()
        demo_batch_prediction()
        
        print("\n" + "="*80)
        print("✅ All demos completed successfully!")
        print("="*80)
        print("\n📖 API Documentation:")
        print(f"  Swagger UI: {API_BASE_URL}/docs")
        print(f"  ReDoc: {API_BASE_URL}/redoc")
        
    except Exception as e:
        logger.error(f"❌ Demo failed: {e}")
        print(f"\n❌ Error: {e}")
        print("\nMake sure the API server is running on http://localhost:8000")


if __name__ == "__main__":
    main()
