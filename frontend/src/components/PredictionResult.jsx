function PredictionResult({ data }) {
  const pred = data.prediction
  const probability = pred.failure_probability

  let statusClass = 'status-ok'
  let statusIcon = '🟢'
  let statusText = 'OK - Normal Operation'

  if (probability < 0.3) {
    statusClass = 'status-ok'
    statusIcon = '🟢'
    statusText = 'OK - Normal Operation'
  } else if (probability < 0.6) {
    statusClass = 'status-caution'
    statusIcon = '🟡'
    statusText = 'CAUTION - Monitor Closely'
  } else if (probability < 0.85) {
    statusClass = 'status-warning'
    statusIcon = '🟠'
    statusText = 'WARNING - Potential Issues'
  } else {
    statusClass = 'status-urgent'
    statusIcon = '🔴'
    statusText = 'URGENT - Failure Risk'
  }

  return (
    <div className="prediction-result">
      <div style={{ textAlign: 'center', marginBottom: '20px' }}>
        <div className="status-icon">{statusIcon}</div>
        <span className={`status-badge ${statusClass}`}>{statusText}</span>
      </div>

      <div className="metric">
        <span className="metric-label">Aircraft ID:</span>
        <span className="metric-value">{data.aircraft_id}</span>
      </div>
      <div className="metric">
        <span className="metric-label">Component ID:</span>
        <span className="metric-value">{data.component_id}</span>
      </div>
      <div className="metric">
        <span className="metric-label">Prediction:</span>
        <span className="metric-value">{pred.prediction_label}</span>
      </div>
      <div className="metric">
        <span className="metric-label">Failure Probability:</span>
        <span className="metric-value">{(probability * 100).toFixed(2)}%</span>
      </div>
      <div className="metric">
        <span className="metric-label">Confidence:</span>
        <span className="metric-value">{pred.confidence.toFixed(2)}%</span>
      </div>

      <div className="action-text">
        <strong>Recommended Action:</strong>
        <br />
        {pred.recommended_action}
      </div>

      <div
        className="metric"
        style={{
          marginTop: '15px',
          paddingTop: '15px',
          borderTop: '1px solid #e0e0e0'
        }}
      >
        <span className="metric-label">Timestamp:</span>
        <span className="metric-value">{new Date().toLocaleString()}</span>
      </div>
    </div>
  )
}

export default PredictionResult
