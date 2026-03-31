"""
Model Loading and Inference Module
Handles model, scaler, and feature management
"""

import joblib
from pathlib import Path
import numpy as np
import pandas as pd
from typing import List, Dict, Any
import logging
import os
import sys

logger = logging.getLogger(__name__)


class PredictiveMaintenanceModel:
    """Wrapper class for the aircraft maintenance prediction model"""
    
    def __init__(self, model_path: str = None,
                 scaler_path: str = None,
                 feature_names_path: str = None):
        """
        Initialize the model by loading artifacts
        
        Args:
            model_path: Path to saved model
            scaler_path: Path to saved scaler
            feature_names_path: Path to saved feature names
        """
        # Resolve paths using pathlib.Path (more robust with spaces)
        script_file = Path(__file__).resolve()  # Full absolute path to model.py
        script_dir = script_file.parent  # .../src
        project_root = script_dir.parent  # .../
        artifacts_dir = project_root / "notebooks" / "artifacts"  # .../notebooks/artifacts (absolute Path object)
        
        # Build artifact paths - always resolve from artifacts_dir, not from cwd
        # Use artifacts_dir directly since it's computed correctly from script location
        if model_path:
            # If custom path provided, resolve it relative to project root
            custom_path = Path(model_path)
            if custom_path.is_absolute():
                self.model_path = str(custom_path.resolve())
            else:
                # Resolve relative path from project root (safer than from script_dir)
                self.model_path = str((project_root / custom_path).resolve())
        else:
            # Use pre-computed artifacts_dir directly
            self.model_path = str(artifacts_dir / "best_model.pkl")
            
        if scaler_path:
            custom_path = Path(scaler_path)
            if custom_path.is_absolute():
                self.scaler_path = str(custom_path.resolve())
            else:
                self.scaler_path = str((project_root / custom_path).resolve())
        else:
            self.scaler_path = str(artifacts_dir / "scaler.pkl")
            
        if feature_names_path:
            custom_path = Path(feature_names_path)
            if custom_path.is_absolute():
                self.feature_names_path = str(custom_path.resolve())
            else:
                self.feature_names_path = str((project_root / custom_path).resolve())
        else:
            self.feature_names_path = str(artifacts_dir / "feature_names.pkl")
        
        # Log paths for debugging
        logger.info(f"📂 Project root: {project_root}")
        logger.info(f"📂 Artifacts dir: {artifacts_dir}")
        logger.info(f"📂 Model path: {self.model_path}")
        logger.info(f"📂 Model exists: {os.path.exists(self.model_path)}")
        
        # Verify paths exist
        if not os.path.exists(self.model_path):
            logger.error(f"❌ Model file not found: {self.model_path}")
        if not os.path.exists(self.scaler_path):
            logger.error(f"❌ Scaler file not found: {self.scaler_path}")
        if not os.path.exists(self.feature_names_path):
            logger.error(f"❌ Feature names file not found: {self.feature_names_path}")
        
        # Load artifacts
        self.model = None
        self.scaler = None
        self.feature_names = None
        self.load_artifacts()
        
        logger.info("✅ Model initialized successfully")
    
    def load_artifacts(self):
        """Load model, scaler, and feature names from disk"""
        try:
            # Load model
            self.model = joblib.load(self.model_path)
            logger.info(f"✅ Model loaded from {self.model_path}")
            
            # Load scaler
            self.scaler = joblib.load(self.scaler_path)
            logger.info(f"✅ Scaler loaded from {self.scaler_path}")
            
            # Load feature names
            self.feature_names = joblib.load(self.feature_names_path)
            logger.info(f"✅ Feature names loaded from {self.feature_names_path}")
            
            # Verify consistency
            assert len(self.feature_names) == self.scaler.n_features_in_, \
                f"Mismatch: {len(self.feature_names)} features vs {self.scaler.n_features_in_} scaler features"
                
        except FileNotFoundError as e:
            logger.error(f"❌ Error loading artifacts: {e}")
            raise
        except Exception as e:
            logger.error(f"❌ Unexpected error loading artifacts: {e}")
            raise
    
    def predict_single(self, features: Dict[str, float]) -> Dict[str, Any]:
        """
        Make a prediction for a single sample
        
        Args:
            features: Dictionary with feature names and values
            
        Returns:
            Dictionary with prediction, probability, and confidence
        """
        try:
            # Validate features
            self._validate_features(features)
            
            # Convert to DataFrame
            X = pd.DataFrame([features])
            
            # Ensure column order matches training
            X = X[self.feature_names]
            
            # Scale features
            X_scaled = self.scaler.transform(X)
            
            # Get prediction
            prediction = self.model.predict(X_scaled)[0]
            probability = self.model.predict_proba(X_scaled)[0]
            
            # Interpret results
            failure_prob = probability[1]
            confidence = max(probability) * 100
            
            return {
                "prediction": int(prediction),
                "prediction_label": "FAILURE" if prediction == 1 else "NO FAILURE",
                "failure_probability": float(failure_prob),
                "no_failure_probability": float(probability[0]),
                "confidence": float(confidence),
                "recommended_action": self._get_recommendation(prediction, failure_prob)
            }
            
        except Exception as e:
            logger.error(f"❌ Prediction error: {e}")
            raise
    
    def predict_batch(self, features_list: List[Dict[str, float]]) -> List[Dict[str, Any]]:
        """
        Make predictions for multiple samples
        
        Args:
            features_list: List of feature dictionaries
            
        Returns:
            List of prediction dictionaries
        """
        predictions = []
        for features in features_list:
            pred = self.predict_single(features)
            predictions.append(pred)
        return predictions
    
    def _validate_features(self, features: Dict[str, float]):
        """Validate that all required features are present and valid"""
        missing_features = set(self.feature_names) - set(features.keys())
        if missing_features:
            raise ValueError(f"❌ Missing required features: {missing_features}")
        
        extra_features = set(features.keys()) - set(self.feature_names)
        if extra_features:
            logger.warning(f"⚠️ Extra features provided (will be ignored): {extra_features}")
        
        # Check for non-numeric values
        for feature, value in features.items():
            if feature not in self.feature_names:
                continue
            try:
                float(value)
            except (TypeError, ValueError):
                raise ValueError(f"❌ Feature '{feature}' must be numeric, got {type(value)}")
    
    def _get_recommendation(self, prediction: int, failure_prob: float) -> str:
        """Generate maintenance recommendation based on prediction"""
        if prediction == 1:
            if failure_prob >= 0.8:
                return "🔴 URGENT: Schedule maintenance immediately. High failure risk detected."
            else:
                return "🟠 WARNING: Schedule maintenance soon. Potential failure risk detected."
        else:
            if failure_prob >= 0.3:
                return "🟡 CAUTION: Monitor closely. Some risk indicators present."
            else:
                return "🟢 OK: Continue normal operations. No immediate maintenance needed."
    
    def get_model_info(self) -> Dict[str, Any]:
        """Get information about the loaded model"""
        return {
            "model_type": type(self.model).__name__,
            "number_of_features": len(self.feature_names),
            "feature_names": list(self.feature_names),
            "model_performance": {
                "test_recall": 1.0,
                "test_precision": 0.6290,
                "test_f1_score": 0.7723,
                "test_roc_auc": 0.9928
            },
            "imbalance_handling": "SMOTE",
            "scaling_method": "StandardScaler",
            "artifact_paths": {
                "model": str(self.model_path),
                "scaler": str(self.scaler_path),
                "features": str(self.feature_names_path)
            }
        }
