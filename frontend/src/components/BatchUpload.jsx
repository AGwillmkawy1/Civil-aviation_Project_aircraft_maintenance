import { useState } from 'react'
import { api } from '../api/client'

function BatchUpload({ onError, onLoadingChange }) {
  const [batchResults, setBatchResults] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleFileUpload = (e) => {
    const file = e.target.files[0]
    if (!file) return

    const reader = new FileReader()
    reader.onload = (event) => {
      const csv = event.target.result
      const lines = csv.trim().split('\n')
      const headers = lines[0].split(',').map((h) => h.trim())

      const components = []
      for (let i = 1; i < lines.length; i++) {
        const values = lines[i].split(',').map((v) => v.trim())
        const component = {}
        headers.forEach((header, index) => {
          component[header] = isNaN(values[index]) ? values[index] : parseFloat(values[index])
        })
        components.push(component)
      }

      processBatch(components)
    }
    reader.readAsText(file)
  }

  const processBatch = async (components) => {
    setLoading(true)
    onLoadingChange(true)
    onError(null)

    try {
      const response = await api.predictBatch(components)
      setBatchResults(response.data)
    } catch (error) {
      const errorMsg = error.response?.data?.detail || error.message
      onError(`Connection Error: ${errorMsg}`)
    } finally {
      setLoading(false)
      onLoadingChange(false)
    }
  }

  return (
    <div className="card">
      <h2>📁 Batch Prediction Upload</h2>

      <label htmlFor="csv-upload" className="batch-upload">
        <p style={{ marginBottom: '10px' }}>📤 Click here to upload CSV file</p>
        <p style={{ color: '#999', fontSize: '0.9em' }}>
          Format: Each row = one component with all 31 features
        </p>
        <input
          id="csv-upload"
          type="file"
          accept=".csv"
          onChange={handleFileUpload}
          style={{ display: 'none' }}
        />
      </label>

      {loading && (
        <div className="loading">
          <div className="spinner"></div>
          <p>Processing batch...</p>
        </div>
      )}

      {batchResults && !loading && (
        <div>
          <div className="success">
            ✅ Batch processed successfully!
            <br />
            Total: {batchResults.total_predictions} | Failures: {batchResults.failures_detected}
          </div>

          <div className="batch-summary">
            <div className="summary-card">
              <div className="summary-value">{batchResults.total_predictions}</div>
              <div className="summary-label">Total Predictions</div>
            </div>
            <div className="summary-card">
              <div className="summary-value" style={{ color: '#c53030' }}>
                {batchResults.failures_detected}
              </div>
              <div className="summary-label">Failures Detected</div>
            </div>
            <div className="summary-card">
              <div className="summary-value" style={{ color: '#22863a' }}>
                {batchResults.total_predictions - batchResults.failures_detected}
              </div>
              <div className="summary-label">Normal Components</div>
            </div>
          </div>

          <table className="results-table">
            <thead>
              <tr>
                <th>Aircraft</th>
                <th>Component</th>
                <th>Status</th>
                <th>Probability</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              {batchResults.predictions.map((pred, idx) => {
                const probability = (pred.failure_probability * 100).toFixed(2)
                let icon = '🟢'
                if (probability < 30) icon = '🟢'
                else if (probability < 60) icon = '🟡'
                else if (probability < 85) icon = '🟠'
                else icon = '🔴'

                return (
                  <tr key={idx}>
                    <td>{pred.aircraft_id}</td>
                    <td>{pred.component_id}</td>
                    <td>
                      {icon} {pred.prediction_label}
                    </td>
                    <td>{probability}%</td>
                    <td style={{ fontSize: '0.9em' }}>
                      {pred.recommended_action.substring(0, 50)}...
                    </td>
                  </tr>
                )
              })}
            </tbody>
          </table>
        </div>
      )}
    </div>
  )
}

export default BatchUpload
