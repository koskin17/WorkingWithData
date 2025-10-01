# Задание 1: Скачайте с сайта https://grouplens.org/datasets/movielens/ датасет любого размера. Определите какому фильму было выставлено больше всего оценок 5.0.
import pandas as pd

dataframe = pd.read_csv('Lesson 12 Pandas/ml-latest-small/ratings.csv').sort_values(by='rating', ascending=False).filter(items=['movieId', 'rating'])
rating = 5
data = dataframe[dataframe['rating'] == rating]['movieId'].value_counts()

print(data)

# Задание 2: По данным файла power.csv посчитайте суммарное потребление стран Прибалтики (Латвия, Литва и Эстония) категорий 4, 12 и 21 за период с 2005 по 2010 года. Не учитывайте в расчетах отрицательные значения quantity.

# Задание 3: Выберите страницу любого сайта с табличными данными. Импортируйте таблицы в pandas dataframe.
# Примеры страниц (необязательно брать именно эти):
# https://fortrader.org/quotes