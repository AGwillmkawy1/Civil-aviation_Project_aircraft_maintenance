# 🚀 Deployment Guide: Aircraft Predictive Maintenance System

**Status:** ✅ Project fully functional and ready for distribution
**Environment:** Python 3.13.3 + Virtual Environment
**Components:** FastAPI Backend + React Frontend + ML Model

---

## Quick Summary: What's Ready

| Component | Status | Location |
|-----------|--------|----------|
| ML Model | ✅ Trained (98.76% Recall) | `notebooks/artifacts/` |
| Backend API | ✅ FastAPI ready | `src/main.py` |
| Frontend | ✅ React Vite | `frontend/` |
| Virtual Env | ✅ Configured | `.venv/` |
| Documentation | ✅ Complete | LaTeX reports + guides |

---

## 🎯 Deployment Options (Ranked by Ease)

### **OPTION 1: GitHub (Recommended for Team/Community)**
**Best for:** Collaboration, version control, free hosting options

#### Step 1: Initialize Git Repository
```bash
cd c:\Users\Student\Downloads\Civil\ aviation_Project_aircraft_maintenance

# Initialize Git
git init
git add .
git commit -m "Initial commit: Aircraft Predictive Maintenance System"

# Create .gitignore to exclude venv and large files
echo ".venv/
*.pyc
__pycache__/
*.pkl
node_modules/
.DS_Store
.env" > .gitignore

git add .gitignore
git commit -m "Add .gitignore"
```

#### Step 2: Create GitHub Repository
1. Go to **github.com** → Sign in
2. Click **+** → **New repository**
3. Name: `aircraft-predictive-maintenance`
4. Description: `ML system for predicting aircraft component failures (98.76% recall)`
5. Public/Private: Choose based on preference
6. Click **Create repository**

#### Step 3: Push to GitHub
```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/aircraft-predictive-maintenance.git
git push -u origin main
```

**Result:** Your project is now on GitHub! Share link: `https://github.com/YOUR_USERNAME/aircraft-predictive-maintenance`

---

### **OPTION 2: Docker (Easy Setup for Users)**
**Best for:** Guaranteed same environment across all machines

#### Step 1: Create Dockerfile
Create `Dockerfile` in project root:

```dockerfile
FROM python:3.13-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy backend requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose ports
EXPOSE 8000 5173

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run backend on startup
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### Step 2: Create docker-compose.yml
```yaml
version: '3.8'

services:
  backend:
    build: .
    ports:
      - "8000:8000"
    environment:
      - PYTHONUNBUFFERED=1
    volumes:
      - ./src:/app/src
      - ./notebooks/artifacts:/app/notebooks/artifacts
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  frontend:
    image: node:18-alpine
    working_dir: /app/frontend
    ports:
      - "5173:5173"
    volumes:
      - ./frontend:/app/frontend
    command: bash -c "npm install && npm run dev"
    depends_on:
      - backend
```

#### Step 3: Build & Run with Docker
```bash
# Build image
docker build -t aircraft-maintenance:latest .

# Run container
docker run -p 8000:8000 aircraft-maintenance:latest

# Or use docker-compose
docker-compose up
```

**Users can now run:** `docker-compose up` and everything works!

---

### **OPTION 3: Railway.app (1-Click Deploy)**
**Best for:** Simplest cloud deployment (free tier available)

#### Step 1: Push to GitHub (uses Option 1 above)

#### Step 2: Deploy to Railway
1. Go to **railway.app**
2. Click **New Project** → **Deploy from GitHub**
3. Select your `aircraft-predictive-maintenance` repository
4. Configure:
   - Environment: `Python`
   - Python Version: `3.13`
   - Start Command: `uvicorn src.main:app --host 0.0.0.0 --port $PORT`

#### Step 3: Add Environment Variables
```
PYTHONUNBUFFERED=1
PORT=8000
```

**Result:** App automatically deploys on every GitHub push!
**Access:** `https://your-app-name.up.railway.app`

---

### **OPTION 4: Heroku (with GitHub Integration)**
**Best for:** Portfolio projects, easy CI/CD

#### Step 1: Create Procfile
```
web: uvicorn src.main:app --host 0.0.0.0 --port $PORT
```

#### Step 2: Create runtime.txt
```
python-3.13.3
```

#### Step 3: Deploy
```bash
# Install Heroku CLI, then:
heroku login
heroku create aircraft-maintenance
git push heroku main
```

**Access:** `https://aircraft-maintenance.herokuapp.com`

---

### **OPTION 5: AWS/Azure (Production-Grade)**
**Best for:** Real production deployment, scalability

#### AWS Option (Lambda + API Gateway)
```bash
# Install serverless framework
npm install -g serverless

# Deploy FastAPI to Lambda
serverless deploy function -f api
```

#### Azure Option (Azure App Service)
```bash
# Install Azure CLI
az login
az webapp up --name aircraft-maintenance --runtime "python:3.13"
```

---

## 📦 Package & Share with Users

### Option A: Via GitHub (Easiest)
1. Users clone: `git clone https://github.com/YOUR_USERNAME/aircraft-predictive-maintenance.git`
2. Create venv: `python -m venv venv`
3. Install: `pip install -r requirements.txt`
4. Run backend: `uvicorn src.main:app --reload`
5. Run frontend: `cd frontend && npm install && npm run dev`

### Option B: Via Docker Hub (One Command)
```bash
# Users just run:
docker run -p 8000:8000 YOUR_USERNAME/aircraft-maintenance:latest
```

To push to Docker Hub:
```bash
docker login
docker tag aircraft-maintenance YOUR_USERNAME/aircraft-maintenance:latest
docker push YOUR_USERNAME/aircraft-maintenance:latest
```

### Option C: Via Packaged Release
1. Create release ZIP file with:
   - Source code
   - Pre-installed venv (heavy but works immediately)
   - Setup scripts
   - README

---

## 🚀 RECOMMENDED DEPLOYMENT PATH (For Teams)

Based on your project requirements, here's the best approach:

### **Phase 1: Immediate (This Week)**
```
✅ Push to GitHub
   - Complete version control
   - Backup of your work
   - Easy sharing link
   
✅ Create Docker image
   - Consistent environment
   - No "works on my machine" issues
   - Users run: docker-compose up
```

### **Phase 2: Team Access (Next Week)**
```
✅ Deploy to Railway/Heroku
   - Live backend URL
   - Frontend accessible via web
   - No local setup needed
   - Share live link: https://aircraft-maintenance.railway.app
```

### **Phase 3: Production (Month 1)**
```
✅ AWS/Azure deployment
   - Scalable infrastructure
   - Professional monitoring
   - Usage analytics
   - Can handle 1000+ users
```

---

## 📝 Setup Instructions for Users

Create `DEPLOYMENT_INSTRUCTIONS.md`:

```markdown
# How to Run Aircraft Predictive Maintenance

## Option 1: Quick Start (Docker) ⚡
```bash
docker-compose up
# Backend: http://localhost:8000
# Frontend: http://localhost:5173
# API Docs: http://localhost:8000/docs
```

## Option 2: Local Setup (10 minutes)
```bash
# 1. Clone repository
git clone https://github.com/YOUR_USERNAME/aircraft-predictive-maintenance.git
cd aircraft-predictive-maintenance

# 2. Create virtual environment
python -m venv venv

# 3. Activate (Windows)
.venv\Scripts\activate
# Or (Mac/Linux)
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run backend (Terminal 1)
cd src
uvicorn main:app --reload

# 6. Run frontend (Terminal 2)
cd frontend
npm install
npm run dev

# 7. Open browser
# API: http://localhost:8000/docs
# Frontend: http://localhost:5173
```

## Option 3: Online (No Installation)
Visit: `https://aircraft-maintenance.railway.app` (coming soon)

## API Usage Example
```python
import requests

data = {
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

response = requests.post(
    "http://localhost:8000/predict",
    json=data
)
print(response.json())
```
```

---

## 🔐 Security Checklist

Before going public:

- [ ] Remove any hardcoded API keys
- [ ] Add `.env` support for secrets
- [ ] Update CORS settings (GitHub option: `ALLOWED_ORIGINS`)
- [ ] Enable HTTPS on deployment
- [ ] Add rate limiting to API
- [ ] Set up request validation
- [ ] Create API key system for production

Add to `src/main.py`:
```python
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter

@app.get("/predict")
@limiter.limit("100/minute")  # 100 requests per minute
async def predict(request: Request, data: AircraftComponent):
    # ...
```

---

## 📊 Project Sharing Checklist

Before sharing with team/public:

- [ ] GitHub repository created & public
- [ ] README.md with clear instructions
- [ ] DEPLOYMENT_INSTRUCTIONS.md in root
- [ ] requirements.txt updated
- [ ] .gitignore prevents .venv upload
- [ ] Dockerfile working locally
- [ ] docker-compose tested
- [ ] LaTeX reports included
- [ ] API documentation at `/docs`
- [ ] Example Jupyter notebook
- [ ] License added (MIT recommended)

---

## 🎯 MY RECOMMENDATION FOR YOU

**Right now (15 minutes):**
1. Initialize Git: `git init && git add . && git commit -m "Initial"`
2. Create GitHub repository
3. Push: `git push -u origin main`

**Next hours:**
1. Create `Dockerfile`
2. Test: `docker-compose up`
3. Push to GitHub

**Tomorrow:**
1. Deploy to Railway.app (just click "Deploy")
2. Share live link: `https://your-app.railway.app`
3. Give teammates `docker-compose up` instructions

**End of week:**
1. Production setup (AWS if needed)
2. Monitoring & analytics
3. CI/CD pipeline

---

## 📞 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| "Can't find model" | Ensure artifacts in `notebooks/artifacts/` |
| "Port 8000 in use" | Change: `uvicorn src.main:app --port 8001` |
| "CORS error" | Update `ALLOWED_ORIGINS` in `src/main.py` |
| "Module not found" | Ensure venv activated before running |
| "Docker permission denied" | Run with: `sudo docker-compose up` |

---

## 📞 Resources

- **GitHub Setup:** https://docs.github.com/en/get-started/quickstart/hello-world
- **Docker Docs:** https://docs.docker.com/get-started/
- **Railway Docs:** https://docs.railway.app/get-started
- **FastAPI Deployment:** https://fastapi.tiangolo.com/deployment/
- **React Vite Deploy:** https://vitejs.dev/guide/build.html

---

**You're ready to go! 🚀 Choose Option 1 (GitHub) today, then pick your deployment method tomorrow.**
