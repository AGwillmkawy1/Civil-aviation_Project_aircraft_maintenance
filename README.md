# ✈️ Aircraft Predictive Maintenance System

ML-powered system for predicting aircraft component failures before they occur.

## 📊 Key Metrics
- **Recall:** 100% (catches all failures)
- **Precision:** 52.3% (accurate alerts)
- **ROC-AUC:** 98.76% (excellent discrimination)
- **Model:** Logistic Regression (12 sensor inputs)

## 🏗️ Architecture

```
Frontend (React + Vite)     Backend (FastAPI)      ML Model
     ↓                           ↓                     ↓
http://localhost:5173  ←→  http://localhost:8000  ← Predictions
```

## 🚀 Quick Start

**Terminal 1 - Backend:**
```bash
cd c:\Users\Student\Downloads\Civil aviation_Project_aircraft_maintenance
.\.venv\Scripts\python.exe src/main.py
```

**Terminal 2 - Frontend:**
```bash
cd c:\Users\Student\Downloads\Civil aviation_Project_aircraft_maintenance\frontend
npm run dev
```

Then open: **http://localhost:5173**

---

## 📁 Project Structure

```
.
├── src/                    # Backend API (FastAPI)
│   ├── main.py            # FastAPI app with 6 endpoints
│   ├── model.py           # ML model wrapper
│   └── client.py          # Python client library
├── frontend/              # React UI
│   └── src/
│       ├── components/    # UI components
│       ├── App.jsx        # Main component
│       └── api/           # API client
├── notebooks/             # Jupyter analysis
│   └── artifacts/         # Trained model + scaler
├── requirements.txt       # Python dependencies
└── aircraft_maintenance_dataset.csv  # Training data
```

---

## 🔌 API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/health` | GET | System health check |
| `/predict` | POST | Single prediction |
| `/predict_batch` | POST | Batch predictions |
| `/model_info` | GET | Model metadata |
| `/docs` | GET | Swagger UI |

---

## 📊 Example Prediction

**Request:**
```json
{
  "component": {
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
```

**Response:**
```json
{
  "prediction": 0,
  "prediction_label": "NO FAILURE",
  "failure_probability": 0.02,
  "confidence": 98.5,
  "recommended_action": "Continue normal operations"
}
```

---

## 🔧 Deployment

See `RUN_APP.md` for detailed setup instructions.

---

## 📦 Requirements

- Python 3.13+
- Node.js 18+
- 200MB disk space

---

## ✅ Status
- ✅ Model trained and validated
- ✅ Backend API running
- ✅ Frontend UI responsive
- ✅ All endpoints operational
