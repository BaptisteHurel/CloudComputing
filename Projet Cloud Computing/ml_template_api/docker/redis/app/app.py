# compose_flask/app.py
from flask import Flask
from redis import Redis
#from celery import Celery # https://docs.celeryproject.org/en/stable/getting-started/introduction.html

app = Flask(__name__)
redis = Redis(host='redis-container', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return ' - - - This basic web page has been viewed {} time(s) - - -'.format(redis.get('hits'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

#app = Celery('hello', broker='amqp://guest@localhost//')

#@app.task
#def msg():
    #return 'msg'