from celery import Celery
import functools
import pickle
import json

from app.core.config import Settings, get_app_settings


app_settings: Settings = get_app_settings()

celery_app = Celery("celery")
celery_app.conf.broker_url = app_settings.celery_broker_url
celery_app.conf.result_backend = app_settings.celery_result_backend


class PythonObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        return {"_python_object": pickle.dumps(obj).decode("latin1")}


def as_python_object(dct: dict):
    try:
        return pickle.loads(dct["_python_object"].encode("latin1"))
    except KeyError:
        return dct

# Custom serialization
json.dumps = functools.partial(json.dumps, cls=PythonObjectEncoder)
json.loads = functools.partial(json.loads, object_hook=as_python_object)
