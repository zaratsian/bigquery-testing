
import sys
import datetime
import logging
from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud import bigquery_storage_v1beta1

project_id = 'z12345'

credentials = service_account.Credentials.from_service_account_file(
    'z12345.json',
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

client = bigquery_storage_v1beta1.BigQueryStorageClient(credentials=credentials)

start_time = datetime.datetime.now()

table_ref = bigquery_storage_v1beta1.types.TableReference()
table_ref.project_id = "bigquery-public-data"
table_ref.dataset_id = "chicago_crime"
table_ref.table_id   = "crime"

read_options = bigquery_storage_v1beta1.types.TableReadOptions()
#read_options.selected_fields.append("var1")
#read_options.selected_fields.append("var2")
#read_options.row_restriction = 'var2 = "xyz"'

modifiers = None
#if snapshot_millis > 0:
#    modifiers = bigquery_storage_v1beta1.types.TableModifiers()
#    modifiers.snapshot_time.FromMilliseconds(snapshot_millis)

parent = "projects/{}".format(project_id)
session = client.create_read_session(
    table_ref,
    parent,
    table_modifiers=modifiers,
    read_options=read_options,
    format_=bigquery_storage_v1beta1.enums.DataFormat.ARROW,
    sharding_strategy=(bigquery_storage_v1beta1.enums.ShardingStrategy.LIQUID),
)

reader = client.read_rows(
    bigquery_storage_v1beta1.types.StreamPosition(stream=session.streams[0])
)

rows = reader.rows(session)

results = [row for row in rows]

runtime = datetime.datetime.now() - start_time
runtime_seconds = float('{}.{}'.format(runtime.seconds, runtime.microseconds))

print("Got {} unique rows in {} seconds".format( len(results), runtime_seconds ))

#ZEND
