# 🚀 Complete Setup Guide - Aircraft Predictive Maintenance

Full end-to-end setup for the complete system (Backend + React Frontend).

## 📋 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   React Frontend (Port 5173)                 │
│                                                               │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  - Single Prediction Form                              │ │
│  │  - Batch CSV Upload                                    │ │
│  │  - Model Information Display                          │ │
│  │  - Real-time Results & Recommendations               │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────┬───────────────────────────────────────────┘
                  │
              HTTP/Axios
                  │
                  ▼
┌─────────────────────────────────────────────────────────────┐
│               FastAPI Backend (Port 8000)                   │
│                                                               │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  - /predict (Single Predictions)                       │ │
│  │  - /predict_batch (Batch Processing)                  │ │
│  │  - /model_info (Model Metadata)                       │ │
│  │  - /health (Health Check)                             │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────┬───────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────────┐
│         ML Model Layer (Logistic Regression)                 │
│                                                               │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Trained Model: best_model_Logistic_Regression.pkl    │ │
│  │  Feature Scaler: scaler.pkl                           │ │
│  │  Feature Names: feature_names.pkl                     │ │
│  │  Performance: model_metrics.json                      │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## 🔧 Prerequisites

### System Requirements
- **OS**: Windows / macOS / Linux
- **Python**: 3.13+
- **Node.js**: 18+
- **npm**: 9+

### Check Installations
```bash
# Check Python
python --version

# Check Node.js
node --version

# Check npm
npm --version
```

## 📂 Project Structure

```
Civil aviation_Project_aircraft_maintenance/
├── artifacts/                          # ML model artifacts
│   ├── best_model_Logistic_Regression.pkl
│   ├── scaler.pkl
│   ├── feature_names.pkl
│   └── model_metrics.json
├── frontend/                           # React frontend (NEW!)
│   ├── src/
│   │   ├── components/
│   │   ├── api/
│   │   ├── App.jsx
│   │   └── index.css
│   ├── package.json
│   └── index.html
├── src/                                # Backend
│   ├── main.py                         # FastAPI app
│   ├── model.py                        # Model wrapper
│   ├── client.py                       # Python client
│   └── README.md
├── notebooks/                          # Jupyter notebooks
│   └── Aircraft_Predictive_Maintenance.ipynb
├── requirements.txt                    # Python dependencies
└── README.md
```

## ✅ Step-by-Step Setup

### **Step 1: Set Up Virtual Environment (First Time Only)**

```bash
# Navigate to project root
cd "Civil aviation_Project_aircraft_maintenance"

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### **Step 2: Prepare Model Artifacts**

Verify these files exist in `artifacts/` folder:
```
✅ best_model_Logistic_Regression.pkl   (Model file)
✅ scaler.pkl                           (Feature scaler)
✅ feature_names.pkl                    (Feature list)
✅ model_metrics.json                   (Performance metrics)
```

If missing, run the Jupyter notebook to regenerate:
```bash
jupyter notebook notebooks/Aircraft_Predictive_Maintenance.ipynb
```

### **Step 3: Start FastAPI Backend**

# activate the virtual environment
source .venv/Scripts/activate

```bash
# Make sure .venv is activated
cd src

# Start FastAPI server
python main.py

# OR using uvicorn directly:
uvicorn main:app --reload --port 8000
```

Wait for message: `INFO:     Application startup complete`

### **Step 4: Install & Start React Frontend** (New Terminal)

```bash
# Open new terminal/PowerShell (keep backend running!)

# Navigate to frontend folder
cd "Civil aviation_Project_aircraft_maintenance/frontend/src"

# Install dependencies (first time only)
npm install

# Start React development server
npm run dev
```

Wait for message: `VITE v5.x.x  ready in xxx ms`

### **Step 5: Open in Browser**

```
http://localhost:5173
```

You should see the beautiful Aircraft Maintenance UI! 🎉

## 🎯 Testing the System

### **Test 1: Health Check**
```bash
# Terminal/PowerShell
curl http://localhost:8000/health
```

Expected response: `{"status": "ok", ...}`

### **Test 2: Single Prediction**
```bash
# Use Python client
cd src
python client.py
```

### **Test 3: Web UI**
1. Open `http://localhost:5173` in browser
2. Fill in component data
3. Click "🚀 Get Prediction"
4. See real-time results!

## 🖥️ Running Everything (Quick Reference)

### **Terminal 1: Backend (Keep Running)**
```bash
# From project root
.venv\Scripts\activate          # Activate venv (Windows)
cd src
python main.py
```

### **Terminal 2: Frontend (New Terminal)**
```bash
# From project root
cd frontend
npm run dev
```

### **Terminal 3: Optional - Client Testing**
```bash
# From project root
.venv\Scripts\activate
cd src
python client.py
```

## 🌐 API Endpoints

All available at `http://localhost:8000`:

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/` | Welcome page |
| GET | `/health` | Health check |
| GET | `/docs` | Swagger UI (Interactive) |
| GET | `/model_info` | Model metadata |
| POST | `/predict` | Single prediction |
| POST | `/predict_batch` | Batch predictions |

### Interactive API Testing

Open automatically generated Swagger UI:
```
http://localhost:8000/docs
```

## 📊 Frontend Features

### 📊 Single Prediction Tab
- 31 input fields for sensor data
- Real-time prediction
- Failure probability %
- Confidence score
- Recommended maintenance actions
- Color-coded risk levels

### 📁 Batch Upload Tab
- Upload CSV files
- Process 100+ components instantly
- Summary statistics
- Detailed results table

### ℹ️ Model Info Tab
- Performance metrics (Accuracy, Precision, Recall, etc.)
- Model configuration
- Feature count
- Safety guarantees

## 📝 Sample Data Files

### For Single Prediction
Use default sample data in the form - pre-filled with normal aircraft component readings.

### For Batch Upload (CSV)
Create a CSV file with all 31 features:

```csv
aircraft_id,component_id,flight_cycles,engine_hours,temperature_sensor_1,temperature_sensor_2,vibration_sensor,pressure_sensor,fault_code_count,last_maintenance_cycles,sensor_drift_flag,ambient_temperature,humidity,failure_within_10_cycles,temperature_sensor_1_rolling_mean_3,temperature_sensor_2_rolling_mean_3,vibration_sensor_rolling_mean_3,pressure_sensor_rolling_mean_3,engine_hours_rolling_mean_3,flight_cycles_rolling_mean_3,temperature_sensor_1_rolling_std_3,temperature_sensor_2_rolling_std_3,vibration_sensor_rolling_std_3,pressure_sensor_rolling_std_3,engine_hours_rolling_std_3,flight_cycles_rolling_std_3,temperature_sensor_1_delta,temperature_sensor_2_delta,vibration_sensor_delta,pressure_sensor_delta,engine_hours_delta,flight_cycles_delta,temp_vibration_interaction
AC001,ENG_001,150,125.5,75,82,0.35,98,0,45,0,25,60,0,75,82,0.35,98,125.5,150,0.5,0.6,0.02,0.3,0.5,2,0,0,0,0,0,0,26.25
AC002,ENG_002,350,280,95,105,1.85,112,3,280,1,35,85,1,93,103,1.8,110,275,345,2.5,3,0.15,1.5,3,10,2,2.5,0.1,0.5,5,10,176.75
```

## 🐛 Troubleshooting

### Error: "Connection refused" on frontend
✅ **Solution**: Make sure backend is running on port 8000
```bash
# Check if port 8000 is in use:
netstat -an | findstr 8000
```

### Error: "ModuleNotFoundError: No module named 'fastapi'"
✅ **Solution**: Make sure .venv is activated and requirements installed
```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

### Error: "npm ERR! ENOENT"
✅ **Solution**: Install npm dependencies
```bash
cd frontend
npm install
```

### Port already in use
✅ **Solution**: Change port for either service
```bash
# Backend on different port:
python main.py --port 9000

# Frontend on different port:
npm run dev -- --port 3000
```

### Frontend won't connect to API
✅ **Solution**: Check API configuration in `frontend/src/api/client.js`
```javascript
const API_BASE_URL = 'http://localhost:8000'  // Should match backend port
```

## 🚀 Deployment

### Deploy Frontend to Vercel
```bash
cd frontend
npm run build
# Upload 'dist' folder to Vercel
```

### Deploy Backend to Heroku
```bash
# (Add Procfile and requirements.txt matching setup)
git push heroku main
```

### Deploy Both with Docker
See Docker setup guides in respective READMEs.

## 📚 Additional Resources

- [Backend README](src/README.md) - API documentation
- [Frontend README](frontend/README.md) - React setup
- [Jupyter Notebook](notebooks/Aircraft_Predictive_Maintenance.ipynb) - ML details
- [Requirements](requirements.txt) - Python dependencies

## ✨ What's Next?

✅ **Currently:** Full working application with React frontend + FastAPI backend

🚀 **Optional Enhancements:**
- [ ] Docker containerization
- [ ] Database integration for prediction logging
- [ ] Real-time monitoring dashboard
- [ ] Email alerts for urgent failures
- [ ] Mobile app (React Native)
- [ ] Kubernetes deployment

## 📞 Support

**Issues?** Follow this checklist:
1. ✅ Check both servers are running (ports 8000 & 5173)
2. ✅ Verify Python virtual environment is activated
3. ✅ Check npm packages installed in frontend
4. ✅ Verify model artifacts exist in `artifacts/`
5. ✅ Check firewall isn't blocking ports
6. ✅ Review terminal logs for specific errors

---

**🎉 You're all set! Enjoy your aircraft maintenance system!**
