from flask import Flask
from threading import Thread
import logging


app = Flask('Status')


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/')
def home():
    return "I'm currently alive!"

def runme():
  app.run(host='0.0.0.0',port=4869)

def keep_on():
    t = Thread(target=runme)
    t.start()
    