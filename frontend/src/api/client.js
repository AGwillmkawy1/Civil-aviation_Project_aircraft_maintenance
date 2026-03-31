import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000'

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json'
  }
})

export const api = {
  // Health check
  healthCheck: () => apiClient.get('/health'),

  // Get model info
  getModelInfo: () => apiClient.get('/model_info'),

  // Make single prediction
  predictSingle: (componentData) =>
    apiClient.post('/predict', { component: componentData }),

  // Make batch predictions
  predictBatch: (componentsData) =>
    apiClient.post('/predict_batch', { components: componentsData })
}

export default apiClient
