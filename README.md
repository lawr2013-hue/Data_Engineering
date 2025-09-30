# Проект по обработке данных
# Набор данных (исходный источник)
https://www.kaggle.com/datasets/rashadrmammadov/heart-disease-prediction/data
# Набор данных, дублированный на Гугл диск
https://drive.google.com/file/d/19T-Gm5Dovnae7htHjJP2gUt3Tyl6NPp2/view?usp=sharing
## Как воспользоваться?
1. Создайте conda окружение:
conda env create -f environment.yml
2. Активировать conda окружение:
conda activate my_env
3. Запустите скрипт: data_loader.py:
poetry run python data_loader.py


# Результат
<img width="1673" height="304" alt="Result" src="https://github.com/user-attachments/assets/dd3caa93-062a-44dc-8b79-edcfcf8f3098" />

# Анализ данных
<img width="559" height="501" alt="image (7)" src="https://github.com/user-attachments/assets/5eafbd04-9fa9-4e46-828e-4b2467e8c8a1" />

# Данные после обработки
<img width="526" height="503" alt="image" src="https://github.com/user-attachments/assets/be0a5079-caf6-457f-b8b7-f3d5717affc9" />

## Что сделано?
- Объем занимаемой памяти снизился с 125.1 KB до 87.9 KB за счет удаления строк с пропусками.
- Столбцы, содержащие только значения 1 и 0, приведены к булевому типу.
- Столбцы с 2-3 уникальными значениями преобразованы в категориальный тип (category).

### *Процесс приведения типов для DataFrame лежит в файле data_loader.py*


