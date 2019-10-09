
'''
Install / requirements.txt

sudo pip3 install google-cloud-bigquery-storage
sudo pip3 install google-cloud-bigquery
sudo pip3 install google-auth
'''

import sys
import datetime
import logging
from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud import bigquery_storage_v1beta1


queries = [
    'SELECT * FROM `bigquery-public-data.chicago_crime.crime`'
]

if __name__ == "__main__":
    
    logging.basicConfig(level=logging.DEBUG)
    
    try:
        credentials = service_account.Credentials.from_service_account_file(
            'my-sa-key.json',
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )
        bqclient = bigquery.Client(credentials=credentials, project=credentials.project_id)
    except Exception as e:
        logging.error('Failed to establish python BQ client')
        sys.exit()
    
    for query in queries:
        
        try:
            job_config = bigquery.QueryJobConfig()
            job_config.dry_run = True
            job_config.use_query_cache = False
            query_job = bqclient.query(query, location="US", job_config=job_config)
            total_bytes_processed = query_job.total_bytes_processed
            
            start_time = datetime.datetime.now()
            job_config = bigquery.QueryJobConfig()
            job_config.dry_run = False
            job_config.use_query_cache = False
            dataframe = (
                bqclient.query(query, location="US", job_config=job_config)
                .result()
            )
            logging.info('Pandas dataframe contains {} rows'.format(dataframe.total_rows))
            runtime = datetime.datetime.now() - start_time
            runtime_seconds = float('{}.{}'.format(runtime.seconds, runtime.microseconds))
            logging.info('Successfully executed query: {}'.format(query))
            logging.info('Queried {} bytes in {} seconds ({} MB/s)'.format(total_bytes_processed, runtime_seconds, round(((total_bytes_processed/1000000)/runtime_seconds),2) ))
        except Exception as e:
            logging.warning('Failed to execute query: {}.'.format(query))
            logging.warning('Exception: {}'.format(e))

#ZEND
