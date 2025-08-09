from celery import Celery

from app.core.config import Settings, get_app_settings


app_settings: Settings = get_app_settings()

celery = Celery("celery")
celery.conf.broker_url = app_settings.celery_broker_url
celery.conf.result_backend = app_settings.celery_result_backend
celery.conf.update(
    task_serializer='pickle',
    result_serializer='pickle'
)
