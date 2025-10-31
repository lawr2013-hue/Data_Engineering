import requests
from tqdm import tqdm
import pandas as pd

API_URL = "https://api.thecatapi.com/v1/breeds"
OUTPUT_FILENAME = "cat_breeds.csv"

def load_data_from_api(api_url: str) -> list[dict]:
    """
    Загружает данные о породах кошек из API
    """
    response = requests.get(api_url, headers={"Content-Type": "application/json"})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Ошибка запроса: статус {response.status_code}")
        return []

def convert_to_df_and_save(data: list[dict], fname: str) -> pd.DataFrame | None:
    """
    Преобразует данные в DataFrame и сохраняет в CSV
    """
    if data:
        df = pd.DataFrame(data)
        df.to_csv(fname, index=False)
        return df
    return None

def main():
    print("Загрузка данных пород кошек...")
    breeds = load_data_from_api(API_URL)

    print(f"Получено пород: {len(breeds)}")

    df = convert_to_df_and_save(breeds, OUTPUT_FILENAME)

    if df is not None:
        print(df.info())
        if "name" in df.columns:
            print(df["name"].head(10))

if __name__ == "__main__":
    main()
