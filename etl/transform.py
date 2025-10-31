import pandas as pd


def validate_data(df):
    if df.empty:
        print("Ошибка: данные пустые")
        return False
    
    important_columns = ['Age', 'Blood Pressure', 'Heart Rate']
    for col in important_columns:
        if col not in df.columns:
            print(f"Не хватает колонки: {col}")
            return False
    
    if (df['Age'] < 0).any() or (df['Age'] > 120).any():
        print("Возраст за пределами 0-120 лет")
        return False
    
    print("Данные прошли валидацию")
    return True

def transform_data(df):
    df = df.dropna()
    
    df = df.astype({
        'Age': 'int',
        'Cholesterol': 'int', 
        'Blood Pressure': 'int',
        'Heart Rate': 'int',
        'Exercise Hours': 'int',
        'Stress Level': 'int',
        'Blood Sugar': 'int',
        'Family History': 'bool',
        'Diabetes': 'bool', 
        'Obesity': 'bool',
        'Exercise Induced Angina': 'bool',
        'Heart Disease': 'bool'
    })
    
    print(f"По окончанию очистки осталось: {len(df)} строк")
    return df