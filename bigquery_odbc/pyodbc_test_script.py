# Tested on Centos 7, python 2.7.5
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-39)] on linux2

import sys
import pyodbc
import datetime

try:
    conn = pyodbc.connect('DSN=BigQuery', autocommit=True)
    cursor = conn.cursor()
except Exception as e:
    print('[ EXCEPTION ] Error connecting to ODBC driver. {}'.format(e))
    sys.exit()

start = datetime.datetime.now()

try:
    bytes = cursor.execute('SELECT sum(size_bytes)/pow(10,9) as size FROM `bigquery-public-data.chicago_crime.__TABLES__` WHERE table_id = "crime"').fetchall()[0][0] * 1000000000
    
    rows = cursor.execute('SELECT * FROM `bigquery-public-data.chicago_crime.crime`').fetchall()
except Exception as e:
    print('[ ERROR ] Issue executing query. Check the SQL query (including database and table name and try again.')
    sys.exit()

end = datetime.datetime.now()

runtime = ((end - start).seconds)

print('\n[ INFO ] Runtime:    {} minutes'.format(runtime / float(60)))
print('\n[ INFO ] Throughput: {} MB/second'.format((bytes/1000000)/runtime))
print('\n[ INFO ] Row Count:  {} rows'.format(len(rows)))
print('\n[ INFO ] BigQuery ODBC Driver test complete')

#ZEND
