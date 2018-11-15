from flask import Flask, render_template
from cloud_api.settings import *
from cloud_api.aliyun_cloud_api import describeIns,describeSec,modifySec
# ,render

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    # return render('index.html')
    # return "hello"

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/desaliIns')
def des_aliIns():

    cred=[os.getenv('ALIYUN_SECRET_ID'),
          os.getenv('ALIYUN_SECRET_KEY')]

    inst=describeIns(*cred)
    # taskinfo("InstanceId of Inst: {}".format(inst.Instances.Instance.InstanceId))
    # taskdebug(type(inst))
    return inst

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="0.0.0.0")
