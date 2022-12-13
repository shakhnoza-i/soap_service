from multiprocessing import cpu_count
from os import environ


def max_workers():
    return cpu_count()


bind = "0.0.0.0:" + environ.get("PORT", "8000")
max_requests = 2000
worker_class = "sync"
workers = max_workers()
threads = 3
log_level = "info"

env = {"DJANGO_SETTINGS_MODULE": "core.settings"}

reload = False
name = "uchet_soap_service"
