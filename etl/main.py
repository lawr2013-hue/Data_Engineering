import argparse
import os
from dotenv import load_dotenv

from extract import read_data
from transform import transform_data
from load import save_to_parquet, write_to_db

def main():

    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument('--table-name', default='lavrinenko', help='Название таблицы в БД')
    args = parser.parse_args()
    
    print("Начало ETL процесса")
    
    try:
        # 1. Extract - загрузка данных
        print("1. Загрузка данных...")
        df = read_data()
        
        # 2. Transform - обработка данных
        print("2. Обработка данных...") 
        df = transform_data(df)
        
        # 3. Load - сохранение результатов
        print("3. Сохранение данных...")
        save_to_parquet(df)
        write_to_db(df, args.table_name)
        
        print("ETL процесс завершен успешно!")
        
    except Exception as e:
        print(f"Ошибка: {e}")
        exit(1)

if __name__ == "__main__":
    main()