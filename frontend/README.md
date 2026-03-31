# 🛩️ Aircraft Maintenance Frontend - React

Modern React frontend for the Aircraft Predictive Maintenance API.

## 🚀 Getting Started

### Prerequisites
- Node.js 18+
- npm or yarn

### Installation

```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will be available at `http://localhost:5173`

### Build for Production

```bash
npm run build
npm run preview
```

## 📁 Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── PredictionForm.jsx      # Single prediction form
│   │   ├── PredictionResult.jsx    # Display prediction results
│   │   ├── BatchUpload.jsx         # CSV batch upload
│   │   └── ModelInfo.jsx           # Model information display
│   ├── api/
│   │   └── client.js               # API client with axios
│   ├── App.jsx                     # Main app component
│   ├── App.css                     # App-specific styles
│   ├── index.css                   # Global styles
│   └── main.jsx                    # React entry point
├── index.html                      # HTML entry point
├── vite.config.js                  # Vite configuration
├── package.json                    # Dependencies
└── .gitignore                      # Git ignore rules
```

## 🔌 API Integration

The frontend communicates with the FastAPI backend at `http://localhost:8000`

### Available Endpoints

- `GET /health` - Health check
- `POST /predict` - Single prediction
- `POST /predict_batch` - Batch predictions
- `GET /model_info` - Model information

## 🎨 Features

### Single Prediction Tab
- Fill in 31 features for component monitoring
- Real-time prediction with failure probability
- Confidence scoring
- Recommended maintenance actions
- Color-coded risk levels (🟢 OK → 🔴 URGENT)

### Batch Upload Tab
- Upload CSV files with multiple components
- Process predictions instantly
- Summary statistics
- Detailed results table

### Model Info Tab
- View model performance metrics
- Understand model configuration
- Key feature highlights

## 📦 Dependencies

- **React 18** - UI framework
- **Vite** - Build tool & dev server
- **Axios** - HTTP client

## 🔧 Configuration

### API Endpoint
Default: `http://localhost:8000`

To change, edit `src/api/client.js`:
```javascript
const API_BASE_URL = 'http://your-api-url:port'
```

### Development Server
Default port: `5173`

To use a different port:
```bash
npm run dev -- --port 3000
```

## 🎯 How to Use

### Step 1: Start Backend
```bash
cd ../src
uvicorn main:app --reload
```

### Step 2: Start Frontend
```bash
cd frontend
npm install
npm run dev
```

### Step 3: Open in Browser
```
http://localhost:5173
```

### Step 4: Make Predictions!
- Fill in component data
- Click "Get Prediction"
- See real-time results with recommendations

## 📊 Data Format (CSV Upload)

For batch predictions, upload a CSV with headers matching the 31 features:

```csv
aircraft_id,component_id,flight_cycles,engine_hours,temperature_sensor_1,...
AC001,ENG_001,150,125.5,75,...
AC002,ENG_002,350,280,95,...
```

## 🎨 Styling

The app uses a modern gradient design with:
- Purple gradient background
- Clean card-based layout
- Responsive grid system
- Color-coded status indicators
- Smooth animations

All CSS is in `src/index.css` and `src/App.css`

## 🚀 Deployment

### Vercel (Easiest)
```bash
npm run build
# Deploy dist/ folder to Vercel
```

### Docker
```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

RUN npm install -g serve

EXPOSE 5173

CMD ["serve", "-s", "dist", "-l", "5173"]
```

### Nginx
```bash
npm run build
# Serve dist/ folder with Nginx
```

## 🛠️ Troubleshooting

### Port 5173 already in use
```bash
npm run dev -- --port 3000
```

### API connection errors
- Ensure FastAPI server is running on `http://localhost:8000`
- Check CORS is enabled in `src/main.py`
- Verify API endpoint in `src/api/client.js`

### Module not found errors
```bash
rm -rf node_modules package-lock.json
npm install
```

### Hot reload not working
- Check if `vite.config.js` is properly configured
- Restart dev server: `npm run dev`

## 📚 Learn More

- [React Documentation](https://react.dev)
- [Vite Documentation](https://vitejs.dev)
- [Axios Documentation](https://axios-http.com)

## 📝 Notes

- This frontend is optimized for modern browsers (Chrome, Firefox, Safari, Edge)
- Mobile responsive design included
- Automatically parses CSV files for batch predictions
- Real-time data validation in forms

---

**Happy coding! 🚀**
