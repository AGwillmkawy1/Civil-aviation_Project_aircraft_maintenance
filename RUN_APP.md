# 🚀 RUN APPLICATION

## Quick Start (2 Commands)

### Terminal 1: Start Backend
```bash
cd c:\Users\Student\Downloads\Civil aviation_Project_aircraft_maintenance
.\.venv\Scripts\python.exe src/main.py
```

**Backend will run on:** `http://localhost:8000`

---

### Terminal 2: Start Frontend
```bash
cd c:\Users\Student\Downloads\Civil aviation_Project_aircraft_maintenance\frontend
npm run dev
```

**Frontend will run on:** `http://localhost:5173` (or next available port)

---

## Access Points

- **Frontend UI:** http://localhost:5173
- **Backend API Docs:** http://localhost:8000/docs
- **Backend Health:** http://localhost:8000/health

---

## One-Liner (If using Windows - RUN IN CMD)
```cmd
start python .\.venv\Scripts\python.exe src/main.py && cd frontend && npm run dev
```

---

## Architecture
- Backend: FastAPI (Python) - Port 8000
- Frontend: React + Vite (Node.js) - Port 5173+
- Model: Logistic Regression (12 sensors, 98.76% for ROC-AUC, AND 100% recall for catching all failures)
- Database: In-memory (model artifacts)
