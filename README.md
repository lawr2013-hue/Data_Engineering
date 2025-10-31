# Heart Disease Data Engineering Project

## 📋 О проекте
Проект по предмету "Инжиниринг управления данными". Реализован ETL-пакет для обработки данных о заболеваниях сердца с загрузкой в PostgreSQL.

## 🎯 Цели проекта
- Создание процесса обработки данных, который не ломается при ошибках
- Обеспечение качества данных через валидацию
- Автоматизация процесса обработки медицинских данных

## 📊 Данные
**Исходный источник:** [Kaggle - Heart Disease Prediction](https://www.kaggle.com/datasets/rashadrmammadov/heart-disease-prediction/data)  
**Дубликат на Google Drive:** [Скачать данные](https://drive.google.com/file/d/19T-Gm5Dovnae7htHjJP2gUt3Tyl6NPp2/view?usp=sharing)

**Структура данных:**
- 16 признаков включая возраст, давление, холестерин
- Целевая переменная: наличие заболевания сердца
- 900+ записей о пациентах

## 🗂️ Структура проекта
heart-disease-etl/
├── etl/ # ETL пакет
│ ├── extract.py # Загрузка данных
│ ├── transform.py # Очистка и преобразование
│ ├── load.py # Сохранение в БД и файлы
│ └── main.py # Основной скрипт
├── data/ # Данные (в .gitignore)
│ ├── raw/ # Исходные данные
│ └── processed/ # Обработанные данные
├── .env # Переменные окружения
├── .gitignore # Исключения Git
└── README.md # Документация

## 🚀 Быстрый старт

### 1. Клонирование репозитория
git clone https://github.com/your-username/heart-disease-etl.git
cd heart-disease-etl

### 2. Установление зависимостей
pip install pandas sqlalchemy psycopg2-binary python-dotenv

### 3. Запуск ETL процесса
python etl/main.py

python etl/main.py --table-name lavrinenko

## 📈 Результаты обработки
Оптимизация данных
Объем памяти: снижен с 125.1 KB до 87.9 KB (-30%)

Типы данных: оптимизированы для хранения и анализа

Качество: удалены дубликаты и некорректные записи

Визуализации
https://github.com/user-attachments/assets/5eafbd04-9fa9-4e46-828e-4b2467e8c8a1
https://github.com/user-attachments/assets/be0a5079-caf6-457f-b8b7-f3d5717affc9

## 📊 EDA (Exploratory Data Analysis)






Этот проект создан в учебных целях.
