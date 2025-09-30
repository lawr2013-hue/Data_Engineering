import pandas as pd

file_id = "19T-Gm5Dovnae7htHjJP2gUt3Tyl6NPp2"  # ID файла на Google Drive
file_url = f"https://drive.google.com/uc?id={file_id}"

df = pd.read_csv(file_url, delimiter=';') # читаем файл
# Приведение типов столбцов
# Посмотрим на типы столбцов и узнаем о возможных пустых значениях
print(df.dtypes)
print(df.info())

# Удаляем все строки с пропущенными значениями
df_cleaned = df.dropna()

# Приводим типы столбцов
df_cleaned = df_cleaned.astype({
    'Age': 'int',
    'Gender': 'category',
    'Cholesterol': 'int',
    'Blood Pressure': 'int',
    'Heart Rate': 'int',
    'Smoking': 'category',
    'Alcohol Intake': 'category',
    'Exercise Hours': 'int',
    'Family History': 'bool',
    'Diabetes': 'bool',
    'Obesity': 'bool',
    'Stress Level': 'int',
    'Blood Sugar': 'int',
    'Exercise Induced Angina': 'bool',
    'Chest Pain Type': 'object',
    'Heart Disease': 'bool'
})

# Сохраняем обработанный DataFrame
df_cleaned.to_csv('processed_dataset.csv', index=False, sep=';')

print("\nИнформация о DataFrame после очистки и преобразований:")
df_cleaned.info(memory_usage='deep')
