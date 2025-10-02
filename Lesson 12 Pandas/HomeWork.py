# Задание 1: Скачайте с сайта https://grouplens.org/datasets/movielens/ датасет любого размера. Определите какому фильму было выставлено больше всего оценок 5.0.
import pandas as pd

dataframe = pd.read_csv('Lesson 12 Pandas/ml-latest-small/ratings.csv').sort_values(by='rating', ascending=False).filter(items=['movieId', 'rating'])
rating = 5
data = dataframe[dataframe['rating'] == rating]['movieId'].value_counts()

print(data)

# Задание 2: По данным файла power.csv посчитайте суммарное потребление стран Прибалтики (Латвия, Литва и Эстония) категорий 4, 12 и 21 за период с 2005 по 2010 года. Не учитывайте в расчетах отрицательные значения quantity. 'Latvia', 'Lithuania', 'Estonia'
data = pd.read_csv('Lesson 12 Pandas\power.csv')
# Фильтруем dataframe по странам и по категориям
filtered_data = data.query("country in ['Latvia', 'Lithuania', 'Estonia'] and category in [4, 12, 21]")
print(filtered_data)
# Добавляем к фильтрации dataframe по странам, категориям ещё и период между 2005 и 2010 годами
filtered_data = data.query("country in ['Latvia', 'Lithuania', 'Estonia'] and category in [4, 12, 21] and (year >= 2005 and year <= 2010)")
print(filtered_data)
# Добавляем к фильтрации dataframe по странам, категориям, по периоду между 2005 и 2010 годами ещё и чтобы quantity было больше 0
filtered_data = data.query("country in ['Latvia', 'Lithuania', 'Estonia'] and category in [4, 12, 21] and (year >= 2005 and year <= 2010) and quantity > 0")
print(filtered_data)
# Считаем суммарное потребление по quantity
filtered_data = data.query("country in ['Latvia', 'Lithuania', 'Estonia'] and category in [4, 12, 21] and (year >= 2005 and year <= 2010) and quantity > 0")['quantity'].sum()
print(filtered_data)

# Фильтрация и подсчёт суммы потребления в одной команде и через указание столбцов
print(data[(data['country'].isin(['Latvia', 'Lithuania', 'Estonia'])) & (data['category'].isin([4, 12, 21])) & (data['year'] >= 2005) & (data['year'] <= 2010) & (data['quantity'] > 0)]['quantity'].sum())

# Задание 3: Выберите страницу любого сайта с табличными данными. Импортируйте таблицы в pandas dataframe.
# Примеры страниц (необязательно брать именно эти):
# https://fortrader.org/quotes
data = pd.read_html('https://www.ueex.com.ua/exchange-quotations/natural-gas/medium-and-long-term-market/')[5][:5]
print(data)