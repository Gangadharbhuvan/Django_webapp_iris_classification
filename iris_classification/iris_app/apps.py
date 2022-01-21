from django.apps import AppConfig
from django.conf import settings
from pathlib import Path
import joblib
import numpy as np
import sklearn

class IrisAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iris_app'
    iris_model_path = settings.MODELS / "model.joblib"
    model = joblib.load(iris_model_path)
