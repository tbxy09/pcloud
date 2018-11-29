# from local_settings import *
from sowhat.local_settings import *
import os

os.environ["TENCENTCLOUD_SECRET_ID"] = TENCENTCLOUD_SECRET_ID
os.environ["TENCENTCLOUD_SECRET_KEY"] = TENCENTCLOUD_SECRET_KEY
os.environ["ALIYUN_SECRET_ID"] = ALIYUN_SECRET_ID
os.environ["ALIYUN_SECRET_KEY"] = ALIYUN_SECRET_KEY


SECRET_KEY            = 'YOUR_SECRET_KEY'
TC_SECRET_ID          = TENCENTCLOUD_SECRET_ID
TC_SECRET_KEY         = TENCENTCLOUD_SECRET_KEY

# =============
# = Databases =
# =============

DATABASES = {
    'default': {
        'NAME': 'cloud_service',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'cloud_service',
        'PASSWORD': 'tlwn821n',
        'HOST': '127.0.0.1',
        'OPTIONS': {
            "autocommit": True,
        },
    },
}

MONGO_DB = {
    'name': 'newsblur',
    'host': '127.0.0.1',
    'port': 27017
}

MONGODB_SLAVE = {
    'host': '127.0.0.1'
}

# Celery RabbitMQ/Redis Broker
BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_RESULT_BACKEND = BROKER_URL

REDIS = {
    'host': '127.0.0.1',
}
REDIS_PUBSUB = {
    'host': '127.0.0.1',
}
REDIS_STORY = {
    'host': '127.0.0.1',
}

ELASTICSEARCH_FEED_HOSTS = ["127.0.0.1:9200"]
ELASTICSEARCH_STORY_HOSTS = ["127.0.0.1:9200"]

BACKED_BY_AWS = {
    'pages_on_node': False,
    'pages_on_s3': False,
    'icons_on_s3': False,
}

ORIGINAL_PAGE_SERVER = "127.0.0.1:3060"
