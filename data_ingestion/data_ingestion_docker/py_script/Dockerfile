# specify the base image
FROM python:3.9

WORKDIR /app

# copy the data ingestion script for running
COPY . .

# install the python modules
RUN pip install pandas wget sqlalchemy psycopg2

# run the data ingestion script
CMD ["python", "data_ingestion_script.py"]