from celery import shared_task
import time

@shared_task
def hello():
    time.sleep(3)
    print("Celery is here!")