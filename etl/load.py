import pandas as pd
import os
from sqlalchemy import create_engine

def save_to_parquet(df, filename="data/processed/data.parquet"):

    os.makedirs('data/processed', exist_ok=True)
    df.to_parquet(filename, index=False)
    print(f"Сохранено в {filename}")

def write_to_db(df, table_name="lavrinenko"):
    
    data_to_write = df.head(100)
    
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD') 
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    dbname = os.getenv('DB_NAME')
    
    connection_string = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
    engine = create_engine(connection_string)
    
    data_to_write.to_sql(
        name=table_name,
        con=engine,
        if_exists='replace',
        index=False
    )
    
    print(f"Записано {len(data_to_write)} строк в таблицу '{table_name}'")