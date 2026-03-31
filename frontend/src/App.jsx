import { useState } from 'react'
import PredictionForm from './components/PredictionForm'
import PredictionResult from './components/PredictionResult'
import BatchUpload from './components/BatchUpload'
import ModelInfo from './components/ModelInfo'
import './App.css'

function App() {
  const [activeTab, setActiveTab] = useState('single')
  const [predictionResult, setPredictionResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleTabChange = (tab) => {
    setActiveTab(tab)
    setError(null)
  }

  return (
    <div className="container">
      <header>
        <h1>✈️ Aircraft Predictive Maintenance</h1>
        <p>AI-Powered Component Failure Prediction System</p>
      </header>

      <div className="card">
        <div className="tabs">
          <button
            className={`tab-button ${activeTab === 'single' ? 'active' : ''}`}
            onClick={() => handleTabChange('single')}
          >
            📊 Single Prediction
          </button>
          <button
            className={`tab-button ${activeTab === 'batch' ? 'active' : ''}`}
            onClick={() => handleTabChange('batch')}
          >
            📁 Batch Upload
          </button>
          <button
            className={`tab-button ${activeTab === 'info' ? 'active' : ''}`}
            onClick={() => handleTabChange('info')}
          >
            ℹ️ Model Info
          </button>
        </div>

        {/* Single Prediction Tab */}
        {activeTab === 'single' && (
          <div className="tab-content active">
            <div className="main-grid">
              <PredictionForm
                onPredict={(result) => {
                  setPredictionResult(result)
                  setError(null)
                }}
                onError={(err) => setError(err)}
                onLoadingChange={setLoading}
              />
              <div className="card">
                <h2>📈 Prediction Results</h2>
                {loading && (
                  <div className="loading">
                    <div className="spinner"></div>
                    <p>Processing...</p>
                  </div>
                )}
                {error && <div className="error">❌ {error}</div>}
                {predictionResult && !loading && (
                  <PredictionResult data={predictionResult} />
                )}
                {!predictionResult && !loading && !error && (
                  <p style={{ color: '#999', textAlign: 'center' }}>
                    ⏳ Fill in the form and click "Get Prediction"
                  </p>
                )}
              </div>
            </div>
          </div>
        )}

        {/* Batch Upload Tab */}
        {activeTab === 'batch' && (
          <div className="tab-content active">
            <BatchUpload
              onError={(err) => setError(err)}
              onLoadingChange={setLoading}
            />
          </div>
        )}

        {/* Model Info Tab */}
        {activeTab === 'info' && (
          <div className="tab-content active">
            <ModelInfo onError={(err) => setError(err)} />
          </div>
        )}
      </div>
    </div>
  )
}

export default App
