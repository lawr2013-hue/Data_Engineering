import pandas as pd
import os

def read_data():
    file_id = "19T-Gm5Dovnae7htHjJP2gUt3Tyl6NPp2"
    file_url = f"https://drive.google.com/uc?id={file_id}"
    
    df = pd.read_csv(file_url, delimiter=';')
    print(f"Загружено {len(df)} строк")
    
    os.makedirs('data/raw', exist_ok=True)
    df.to_csv('data/raw/raw_data.csv', index=False, sep=';')
    
    return df