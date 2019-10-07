import os
import datetime
from flask import Flask, jsonify
from google.cloud import bigquery
client = bigquery.Client()

app = Flask(__name__)

@app.route('/query')
def query():
    start_time = datetime.datetime.now()
    query_job = client.query(""" SELECT COUNT(*) FROM `bigquery-public-data.chicago_crime.crime` """)
    runtime = (datetime.datetime.now() - start_time).seconds
    results = [row for row in query_job.result()][0][0]
    return jsonify({'results':results, 'runtime':'{} seconds'.format(runtime)})

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=8080)

#ZEND
