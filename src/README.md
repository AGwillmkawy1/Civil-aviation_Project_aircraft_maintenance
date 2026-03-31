# 🛩️ Aircraft Predictive Maintenance - Web Application

Complete end-to-end system for predicting aircraft component failures using machine learning.

## 📋 Overview

This application combines:
- **Trained ML Model** (Logistic Regression with 100% recall)
- **REST API** (FastAPI with real-time predictions)
- **Web UI** (Beautiful interactive frontend)
- **Batch Processing** (CSV file uploads)
- **Model Monitoring** (Performance metrics & metadata)

## 🚀 Quick Start

### Prerequisites
- Python 3.13+
- Virtual environment activated (see workspace setup)
- All packages installed from `requirements.txt`

### Step 1: Start the FastAPI Server

```bash
# Navigate to src directory
cd src

# Option A: Using uvicorn directly
uvicorn main:app --reload --port 8000

# Option B: Using Python
python main.py
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

### Step 2: Open the Web UI

Once the server is running, open your browser:

```
http://localhost:8000/
```

You'll see the beautiful Aircraft Maintenance UI with three tabs.

### Step 3: Make Predictions!

**Option A: Single Prediction**
1. Go to "📊 Single Prediction" tab
2. Fill in component sensor data
3. Click "🚀 Get Prediction"
4. See real-time failure prediction with confidence score

**Option B: Batch Processing**
1. Go to "📁 Batch Upload" tab
2. Upload a CSV file with multiple components
3. Get predictions for all components instantly

**Option C: View Model Info**
1. Go to "ℹ️ Model Info" tab
2. See detailed model performance metrics
3. Understand model configuration

## 📚 Files Structure

```
src/
├── main.py           # FastAPI application (5 endpoints)
├── model.py          # ML model wrapper (inference logic)
├── client.py         # Python client for testing
├── index.html        # Web UI (interactive form + results)
```

## 🔌 API Endpoints

### 1. GET `/`
Welcome page with available endpoints

```bash
curl http://localhost:8000/
```

### 2. GET `/health`
Health check endpoint

```bash
curl http://localhost:8000/health
```

Response:
```json
{
  "status": "ok",
  "message": "Aircraft Maintenance Prediction API is running"
}
```

### 3. POST `/predict`
Make a single prediction

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "component": {
      "aircraft_id": "AC001",
      "component_id": "ENG_001",
      "flight_cycles": 150.0,
      "engine_hours": 125.5,
      "temperature_sensor_1": 75.0,
      ...
    }
  }'
```

### 4. POST `/predict_batch`
Make batch predictions

```bash
curl -X POST http://localhost:8000/predict_batch \
  -H "Content-Type: application/json" \
  -d '{
    "components": [
      { "aircraft_id": "AC001", ... },
      { "aircraft_id": "AC002", ... }
    ]
  }'
```

### 5. GET `/model_info`
Get model metadata and performance metrics

```bash
curl http://localhost:8000/model_info
```

Response:
```json
{
  "status": "success",
  "model_type": "Logistic Regression",
  "number_of_features": 31,
  "model_performance": {
    "accuracy": 0.9167,
    "precision": 0.6290,
    "recall": 1.0,
    "f1": 0.7726,
    "roc_auc": 0.9986
  },
  ...
}
```

## 🧪 Testing the API

### Using Python Client

```bash
cd src
python client.py
```

This runs comprehensive demos:
- ✅ Health check
- ✅ Model information
- ✅ Single predictions (normal & failure scenarios)
- ✅ Batch predictions

### Using cURL

```bash
# Test health
curl http://localhost:8000/health

# Get model info
curl http://localhost:8000/model_info

# Single prediction with normal readings
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '@sample_normal.json'

# Batch prediction
curl -X POST http://localhost:8000/predict_batch \
  -H "Content-Type: application/json" \
  -d '@sample_batch.json'
```

### Using Swagger UI

FastAPI provides interactive API documentation:

```
http://localhost:8000/docs
```

Try each endpoint directly in the browser!

## 📊 Feature Requirements (31 Total)

### Primary Sensors (12 features)
- `aircraft_id` - Aircraft identifier
- `component_id` - Component identifier  
- `flight_cycles` - Number of flight cycles
- `engine_hours` - Total engine running hours
- `temperature_sensor_1` - First temp sensor reading (°C)
- `temperature_sensor_2` - Second temp sensor reading (°C)
- `vibration_sensor` - Motor vibration level (mm/s)
- `pressure_sensor` - System pressure (PSI)
- `fault_code_count` - Number of active faults
- `last_maintenance_cycles` - Cycles since last maintenance
- `sensor_drift_flag` - Sensor drift indicator (0/1)
- `ambient_temperature` - Ambient temperature (°C)
- `humidity` - Relative humidity (%)

### Engineered Features (19 features)
**Rolling Mean (3-cycle window):**
- `temperature_sensor_1_rolling_mean_3`
- `temperature_sensor_2_rolling_mean_3`
- `vibration_sensor_rolling_mean_3`
- `pressure_sensor_rolling_mean_3`
- `engine_hours_rolling_mean_3`
- `flight_cycles_rolling_mean_3`

**Rolling Std Dev (3-cycle window):**
- `temperature_sensor_1_rolling_std_3`
- `temperature_sensor_2_rolling_std_3`
- `vibration_sensor_rolling_std_3`
- `pressure_sensor_rolling_std_3`
- `engine_hours_rolling_std_3`
- `flight_cycles_rolling_std_3`

**Delta Features (change from previous cycle):**
- `temperature_sensor_1_delta`
- `temperature_sensor_2_delta`
- `vibration_sensor_delta`
- `pressure_sensor_delta`
- `engine_hours_delta`
- `flight_cycles_delta`

**Interaction Features:**
- `temp_vibration_interaction` - Temperature × Vibration
- `failure_within_10_cycles` - Target variable

## 🎯 Prediction Interpretation

### Risk Levels (Color Coded)

| Probability | Status | Action |
|------------|--------|--------|
| 0-30% | 🟢 OK | Continue normal operation |
| 30-60% | 🟡 CAUTION | Increase monitoring frequency |
| 60-85% | 🟠 WARNING | Schedule maintenance soon |
| 85-100% | 🔴 URGENT | Immediate intervention required |

### Confidence Score

- **Higher is better** (95%+ is ideal)
- Indicates model certainty in prediction
- Low confidence = consider manual review

## 🔍 Model Performance

Trained on **6,001 aircraft maintenance records** with:
- **Classes**: Balanced via SMOTE (1:1 ratio on 4,800 training samples)
- **Test Set**: 1,201 samples (imbalance preserved at 3.25%)

### Key Metrics
- **Accuracy**: 91.67% ✅
- **Precision**: 62.90% ⚠️ (intentional trade-off for safety)
- **Recall**: 100.00% ✅ (critical for aviation - no missed failures)
- **F1 Score**: 77.26% ✅
- **ROC-AUC**: 99.86% ✅ (excellent discrimination)

### Why 100% Recall?

In aviation, missing a potential failure is unacceptable. The model prioritizes:
1. **Zero false negatives** (catches all failures)
2. Accepts higher false positives (some unnecessary maintenance)
3. Better safe than sorry philosophy

## 🐳 Docker Deployment (Optional)

To containerize the application:

```dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY artifacts/ ./artifacts/

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:
```bash
docker build -t aircraft-maintenance .
docker run -p 8000:8000 aircraft-maintenance
```

## 📝 Sample Data Format (CSV for Batch)

```csv
aircraft_id,component_id,flight_cycles,engine_hours,temperature_sensor_1,...
AC001,ENG_001,150,125.5,75,82,0.35,98,...
AC002,ENG_002,350,280,95,105,1.85,112,...
```

## ⚙️ Configuration

### API Port
Default: `8000`
Change in `main.py` or command line:
```bash
uvicorn main:app --port 9000
```

### Logging
Check logs in terminal for:
- Model loading status
- Prediction requests
- Error details

### CORS
Enabled for:
- `http://localhost:3000` (React dev server)
- `http://localhost:8080` (Vue dev server)
- Add more origins in `main.py` if needed

## 🛠️ Troubleshooting

### Error: "Model artifacts not found"
- Ensure `artifacts/` folder exists with:
  - `best_model_Logistic_Regression.pkl`
  - `scaler.pkl`
  - `feature_names.pkl`
  - `model_metrics.json`

### Error: "Connection refused"
- Make sure FastAPI server is running
- Check port 8000 is not blocked
- Try different port: `uvicorn main:app --port 9000`

### Error: "Missing features"
- Ensure all 31 features are provided
- Check feature names match exactly (case-sensitive)
- See "Feature Requirements" section above

### Slow predictions
- First prediction may be slower (model warm-up)
- Batch predictions are faster than individual calls
- Normal inference: 10-50ms per sample

## 📊 Next Steps

### Enhance the System
1. **Database**: Store predictions for audit trail
2. **Monitoring**: Track model performance over time
3. **Retraining**: Automate model updates with new data
4. **Alerts**: Email/SMS notifications for urgent failures
5. **Dashboard**: Aggregate fleet-wide statistics

### Deploy to Cloud
- AWS: EC2 + RDS
- Google Cloud: Cloud Run + Cloud SQL
- Azure: App Service + SQL Database
- Heroku: Simple PaaS deployment

## 📞 Support

For issues or questions:
1. Check logs in terminal
2. Use `/docs` (Swagger UI) for API testing
3. Review sample data in `client.py`
4. Check notebook for model details

## 📄 License

This project is for educational purposes.

---

**Happy Predicting! ✈️ 🚀**
