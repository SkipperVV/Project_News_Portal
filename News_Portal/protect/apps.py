from django.apps import AppConfig
import redis

class ProtectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'protect'

red=redis.Redis(
    host= 'redis-10049.c100.us-east-1-4.ec2.cloud.redislabs.com',
    port=  10049,
    password='3J6YKt9fQIaye8krHHY1kmUDwFBKAUCy'
)