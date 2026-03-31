import { useState } from 'react'
import { api } from '../api/client'

const SAMPLE_DATA = {
  aircraft_id: 'AC001',
  component_id: 'ENG_001',
  flight_cycles: 150.0,
  engine_hours: 125.5,
  temperature_sensor_1: 75.0,
  temperature_sensor_2: 82.0,
  vibration_sensor: 0.35,
  pressure_sensor: 98.0,
  fault_code_count: 0,
  last_maintenance_cycles: 45.0,
  maintenance_log_flag: 0,
  ambient_temperature: 25.0,
  humidity: 60.0,
  failure_within_10_cycles: 0
}

function PredictionForm({ onPredict, onError, onLoadingChange }) {
  const [formData, setFormData] = useState(SAMPLE_DATA)

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData((prev) => ({
      ...prev,
      [name]: isNaN(value) ? value : parseFloat(value)
    }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    onLoadingChange(true)
    onError(null)

    try {
      const response = await api.predictSingle(formData)
      onPredict(response.data)
    } catch (error) {
      const errorMsg = error.response?.data?.detail || error.message
      onError(`Connection Error: ${errorMsg}. Make sure the API server is running.`)
    } finally {
      onLoadingChange(false)
    }
  }

  return (
    <div className="card">
      <h2>🔧 Component Data Entry</h2>
      <form onSubmit={handleSubmit}>
        {/* Basic Info */}
        <div className="two-column">
          <div className="form-group">
            <label>Aircraft ID</label>
            <input
              type="text"
              name="aircraft_id"
              value={formData.aircraft_id}
              onChange={handleChange}
              placeholder="e.g., AC001"
            />
          </div>
          <div className="form-group">
            <label>Component ID</label>
            <input
              type="text"
              name="component_id"
              value={formData.component_id}
              onChange={handleChange}
              placeholder="e.g., ENG_001"
            />
          </div>
        </div>

        {/* Sensor Readings */}
        <h3>Sensor Readings</h3>
        <div className="feature-grid">
          <div className="form-group">
            <label>Flight Cycles</label>
            <input
              type="number"
              name="flight_cycles"
              value={formData.flight_cycles}
              onChange={handleChange}
              step="0.1"
            />
          </div>
          <div className="form-group">
            <label>Engine Hours</label>
            <input
              type="number"
              name="engine_hours"
              value={formData.engine_hours}
              onChange={handleChange}
              step="0.1"
            />
          </div>
          <div className="form-group">
            <label>Temperature Sensor 1 (°C)</label>
            <input
              type="number"
              name="temperature_sensor_1"
              value={formData.temperature_sensor_1}
              onChange={handleChange}
              step="0.1"
            />
          </div>
          <div className="form-group">
            <label>Temperature Sensor 2 (°C)</label>
            <input
              type="number"
              name="temperature_sensor_2"
              value={formData.temperature_sensor_2}
              onChange={handleChange}
              step="0.1"
            />
          </div>
          <div className="form-group">
            <label>Vibration Sensor (mm/s)</label>
            <input
              type="number"
              name="vibration_sensor"
              value={formData.vibration_sensor}
              onChange={handleChange}
              step="0.01"
            />
          </div>
          <div className="form-group">
            <label>Pressure Sensor (PSI)</label>
            <input
              type="number"
              name="pressure_sensor"
              value={formData.pressure_sensor}
              onChange={handleChange}
              step="0.1"
            />
          </div>
          <div className="form-group">
            <label>Fault Code Count</label>
            <input
              type="number"
              name="fault_code_count"
              value={formData.fault_code_count}
              onChange={handleChange}
              step="1"
            />
          </div>
          <div className="form-group">
            <label>Last Maint. (cycles)</label>
            <input
              type="number"
              name="last_maintenance_cycles"
              value={formData.last_maintenance_cycles}
              onChange={handleChange}
              step="0.1"
            />
          </div>
          <div className="form-group">
            <label>Maintenance Log Flag</label>
            <select
              name="maintenance_log_flag"
              value={formData.maintenance_log_flag}
              onChange={handleChange}
            >
              <option value="0">No</option>
              <option value="1">Yes</option>
            </select>
          </div>
          <div className="form-group">
            <label>Ambient Temp. (°C)</label>
            <input
              type="number"
              name="ambient_temperature"
              value={formData.ambient_temperature}
              onChange={handleChange}
              step="0.1"
            />
          </div>
          <div className="form-group">
            <label>Humidity (%)</label>
            <input
              type="number"
              name="humidity"
              value={formData.humidity}
              onChange={handleChange}
              step="0.1"
            />
          </div>
          <div className="form-group">
            <label>Failure Within 10 Cycles</label>
            <select
              name="failure_within_10_cycles"
              value={formData.failure_within_10_cycles}
              onChange={handleChange}
            >
              <option value="0">No</option>
              <option value="1">Yes</option>
            </select>
          </div>
        </div>

        <button type="submit" style={{ marginTop: '20px' }}>
          🚀 Get Prediction
        </button>
      </form>
    </div>
  )
}

export default PredictionForm
