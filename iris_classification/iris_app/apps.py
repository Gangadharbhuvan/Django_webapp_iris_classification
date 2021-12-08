from django.apps import AppConfig


class IrisAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iris_app'
    iris_model_path = settings.MODELS / "model.joblib"
    model = joblib.load(iris_model_path)
