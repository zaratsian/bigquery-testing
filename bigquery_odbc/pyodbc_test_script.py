

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
    rows = cursor.execute('SELECT * FROM `bigquery-public-data.chicago_crime.crime`').fetchall()
except Exception as e:
    print('[ ERROR ] Issue executing query. Check the SQL query (including database and table name and try again.')
    sys.exit()

end = datetime.datetime.now()

runtime = ((end - start).seconds) / float(60)

print('\n[ INFO ] Runtime:   {}'.format(runtime))
print('\n[ INFO ] Row Count: {}'.format(len(rows)))
print('\n[ INFO ] BigQuery ODBC Driver test complete')

#ZEND
