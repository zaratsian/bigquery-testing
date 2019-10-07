FROM python:3.7-slim

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . ./

RUN pip install Flask gunicorn google-cloud-bigquery

# Run the web service on container startup. Here we use the gunicorn.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app

#ZEND
