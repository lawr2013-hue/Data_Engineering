import pandas as pd

file_id = "19T-Gm5Dovnae7htHjJP2gUt3Tyl6NPp2"  # ID файла на Google Drive
file_url = f"https://drive.google.com/uc?id={file_id}"

raw_data = pd.read_csv(file_url)     # читаем файл

print(raw_data.head(10))

