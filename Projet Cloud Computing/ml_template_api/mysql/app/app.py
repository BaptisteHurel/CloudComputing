from typing import List, Dict
from flask import Flask
import json
from sqlalchemy import create_engine, MetaData, Table, Column, Float, Integer, String, ForeignKey
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.dialects.mysql import DATETIME

import logging

app = Flask(__name__)

config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'classicmodels'
    }

db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
# connect to database
engine = create_engine(connection_str)
connection = engine.connect()
logging.info(' - - - ✅ MySQL Docker Container Python connection ok - - - \n')

metadata = MetaData(bind=engine)
metadata.reflect(only=['customers','employees','offices', 'orderdetails','orders','payments','productlines','products'])


#mapping of metadata
Base = automap_base(metadata=metadata)
Base.prepare()
payments = Base.classes.payments

logging.info('\n - - - ✅ [Tables] Payments | Data Mapping OK - - - \n')

def print_table() -> List:
    tab=[]
    logging.info(' - - - ✅ Tables into database - - - \n')
    for t in metadata.sorted_tables:
        print("\t\t - {}".format(t.name))
        tab.append(t.name)
    return tab 

#create session and perform request 
from sqlalchemy.orm import sessionmaker
from datetime import date
Session = sessionmaker()
# associate session with our db 
Session.configure(bind=engine)
session = Session()

def sample_query() -> List:    
    #query db
    q=[]
    prilogging.info('\n### ✅ All Payments with date > 01 June 2005:')
    pays = session.query(payments)\
        .filter_by(paymentDate > date(2005,6,1))\
        .all()
    for pay in pays:
        q.append('{pay.customerNumber} payed {pay.amount} on {pay.paymentDate}')
    print('')
    return q 

@app.route('/')
def index() -> str:
    return ' - - - ✅ MySQL Database `classicmodels` connection ok - - - '

@app.route('/tables')
def tables() -> str:
    return json.dumps({'Tables ': print_table()})

@app.route('/query')
def sample_query() -> str:
    return json.dumps({'Sample Query ': sample_query()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)

