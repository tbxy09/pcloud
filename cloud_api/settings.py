# from local_settings import *
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


