import wget
import gzip
import pandas as pd
from sqlalchemy import create_engine

import warnings
warnings.filterwarnings("ignore")


print('downloading the dataset in zip format..')
dataset_URL = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz'
wget.download(dataset_URL)

print('creating the dataframe from the zip file..')
data_dictionary_URL = 'https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf'
wget.download(data_dictionary_URL)

with gzip.open('yellow_tripdata_2021-01.csv.gz') as f:
    df = pd.read_csv(f)

print('creating lookup table dataframe..')
lookup_table_URL = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv'
lookup_df = pd.read_csv(lookup_table_URL)


df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])


USER = 'root'
PASSWORD = 'root'
DB = 'nytaxi_db'
HOST = 'db' # 'localhost' for dev version
PORT = 5432

CONNECTION_URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'

print('connecting to the database..')
engine = create_engine(CONNECTION_URL)
engine.connect()

print('inserting into the database..')
table_name = 'yellow_taxi_data_table'
df.to_sql(table_name, con=engine)

print('data ingestion done!!')