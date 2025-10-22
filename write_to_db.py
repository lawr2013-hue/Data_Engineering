import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
dbname = os.getenv('DB_NAME')

connection_string = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
engine = create_engine(connection_string)


df = pd.read_csv('my_project/processed_dataset.csv')  

table_name = 'lavrinenko'

data_to_write = df.head(50)
data_to_write.to_sql(name=table_name, con=engine, schema='public', if_exists='replace', index=False)
print(f"Записано {len(data_to_write)} строк в таблицу '{table_name}' базы {dbname}.")