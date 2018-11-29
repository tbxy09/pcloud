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

# @app.route('/hello')
# def hello():
#     return render_template('hello.html')

@app.route('/rating')
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

@app.route("/db_check/mysql")
def db_check_mysql():
    connect_params = "dbname='%s' user='%s' password='%s' host='%s' port='%s'" % (
        settings.DATABASES['default']['NAME'],
        settings.DATABASES['default']['USER'],
        settings.DATABASES['default']['PASSWORD'],
        settings.DATABASES['default']['HOST'],
        settings.DATABASES['default']['PORT'],
    )
    try:

        conn = MySQLdb.connect(host=settings.DATABASES['default']['HOST'],
                               port=settings.DATABASES['default']['PORT'],
                               user=settings.DATABASES['default']['USER'],
                               passwd=settings.DATABASES['default']['PASSWORD'],
                               db=settings.DATABASES['default']['NAME'])
    except:
        print(" ---> Mysql can't connect to the database: %s" % connect_params)
        abort(502)

    cur = conn.cursor()
    cur.execute("""SELECT id FROM feeds ORDER BY feeds.id DESC LIMIT 1""")
    rows = cur.fetchall()
    for row in rows:
        return unicode(row[0])

    abort(404)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="0.0.0.0")
