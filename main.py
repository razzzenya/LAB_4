import csv
import datetime
import os

import numpy as np
import pandas as pd


def c_to_f(temperature: int) -> int or str:
    """Конвертирует температуру в градусах Цельсия в градусы Фаренгейта

    Args:
        temperature (int): Значение температуры в Цельсиях

    Returns:
        int or str: Возвращаемое значение в Фаренгейтах , либо NaN
    """
    if temperature == np.nan:
        return np.nan

    return (temperature * 9 / 5) + 32


def sort_by_temp(df: pd.DataFrame, temperature: int) -> pd.DataFrame:
    """Функция фильтрует исходный объект DataFrame по температуре

    Args:
        df (pd.DataFrame): Исходный объект
        temperature (int): Температура по которой фильтруется объект DataFrame

    Returns:
        pd.DataFrame: Возвращается отфильтрованный объект DataFrame
    """
    result = pd.DataFrame(columns=['date', 'temperature day', 'pressure day',
                          'wind day', 'temperature night', 'pressure night', 'wind night', 'fahrenheit temperature day', 'fahrenheit temperature night'])
    for i in range(len(df)):

        if df.iloc[i]['temperature day'] >= temperature:

            result.loc[len(result)] = [df.iloc[i]['date'], df.iloc[i]['temperature day'], df.iloc[i]['pressure day'], df.iloc[i]['wind day'], df.iloc[i]['temperature night'],
                                       df.iloc[i]['pressure night'], df.iloc[i]['wind night'], df.iloc[i]['fahrenheit temperature day'], df.iloc[i]['fahrenheit temperature night']]

    return result


def str_transform_datetime(date: str) -> datetime.date:
    """_summary_

    Args:
        date (str): _description_

    Returns:
        datetime.date: _description_
    """
    result = datetime.date(int(date[:4]), int(date[5:7]), int(date[8:10]))
    return result


def sort_by_date_1(df: pd.DataFrame, first_date: datetime.date, second_date: datetime.date) -> pd.DataFrame:
    """Фильтрует DataFrame по двум датам , заданными в datetime.date

    Args:
        df (pd.DataFrame): Исходный объект
        first_date (datetime.date): Первая дата
        second_date (datetime.date): Вторая дата

    Returns:
        pd.DataFrame: Отфильтрованный объект по двум датам
    """
    result = pd.DataFrame(columns=['date', 'temperature day', 'pressure day',
                          'wind day', 'temperature night', 'pressure night', 'wind night', 'fahrenheit temperature day', 'fahrenheit temperature night'])
    flag = False

    for i in range(len(df)):

        if flag == False:

            if df.iloc[i]['date'] == pd.Timestamp(first_date.year, first_date.month, first_date.day):
                flag = True
                result.loc[len(result)] = [df.iloc[i]['date'], df.iloc[i]['temperature day'], df.iloc[i]['pressure day'], df.iloc[i]['wind day'], df.iloc[i]['temperature night'],
                                           df.iloc[i]['pressure night'], df.iloc[i]['wind night'], df.iloc[i]['fahrenheit temperature day'], df.iloc[i]['fahrenheit temperature night']]

        if flag:

            result.loc[len(result)] = [df.iloc[i]['date'], df.iloc[i]['temperature day'], df.iloc[i]['pressure day'], df.iloc[i]['wind day'], df.iloc[i]['temperature night'],
                                       df.iloc[i]['pressure night'], df.iloc[i]['wind night'], df.iloc[i]['fahrenheit temperature day'], df.iloc[i]['fahrenheit temperature night']]

            if df.iloc[i]['date'] == pd.Timestamp(second_date.year, second_date.month, second_date.day):
                break

    return result


def sort_by_date_2(df: pd.DataFrame, first_date: str, second_date: str) -> pd.DataFrame:
    """Фильтрует DataFrame по двум датам , заданными в str

    Args:
        df (pd.DataFrame): Исходный объект
        first_date (datetime.date): Первая дата
        second_date (datetime.date): Вторая дата

    Returns:
        pd.DataFrame: Отфильтрованный объект по двум датам
    """
    result = pd.DataFrame(columns=['date', 'temperature day', 'pressure day',
                          'wind day', 'temperature night', 'pressure night', 'wind night', 'fahrenheit temperature day', 'fahrenheit temperature night'])

    flag = False
    first_date = str_transform_datetime(first_date)
    second_date = str_transform_datetime(second_date)

    for i in range(len(df)):

        if flag == False:

            if df.iloc[i]['date'] == pd.Timestamp(first_date.year, first_date.month, first_date.day):
                flag = True
                result.loc[len(result)] = [df.iloc[i]['date'], df.iloc[i]['temperature day'], df.iloc[i]['pressure day'], df.iloc[i]['wind day'], df.iloc[i]['temperature night'],
                                           df.iloc[i]['pressure night'], df.iloc[i]['wind night'], df.iloc[i]['fahrenheit temperature day'], df.iloc[i]['fahrenheit temperature night']]

        if flag:

            result.loc[len(result)] = [df.iloc[i]['date'], df.iloc[i]['temperature day'], df.iloc[i]['pressure day'], df.iloc[i]['wind day'], df.iloc[i]['temperature night'],
                                       df.iloc[i]['pressure night'], df.iloc[i]['wind night'], df.iloc[i]['fahrenheit temperature day'], df.iloc[i]['fahrenheit temperature night']]

            if df.iloc[i]['date'] == pd.Timestamp(second_date.year, second_date.month, second_date.day):
                break

    return result


def group_df(df: pd.DataFrame) -> pd.DataFrame:
    """_summary_

    Args:
        df (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """

    result = pd.DataFrame(
        columns=['date', 'average temperature day', 'average temperature night', 'fahrenheit temperature day', 'fahrenheit temperature night'])

    avg_arr = []
    dates_arr = []

    temp_month_arr = []

    for i in range(len(df)):

        pass


path = 'dataset.csv'
with open(path, 'r', encoding='utf-8') as file:
    data = list(csv.reader(file, delimiter=","))

    dates = []
    temperature_day = []
    pr_day = []
    wind_day = []
    temperature_night = []
    pr_night = []
    wind_night = []

    for i in data:

        dates.append(i[0])
        temperature_day.append(i[1])
        pr_day.append(i[2])
        wind_day.append(i[3])
        temperature_night.append(i[4])
        pr_night.append(i[5])
        wind_night.append(i[6])


# объект DataFrame

df = pd.DataFrame({
    'date': dates,
    'temperature day': temperature_day,
    'pressure day': pr_day,
    'wind day': wind_day,
    'temperature night': temperature_night,
    'pressure night': pr_night,
    'wind night': wind_night
})

df['date'] = pd.to_datetime(df['date'])

# обработка пропущенных значений

df['temperature day'] = pd.to_numeric(df['temperature day'], errors='coerce')
df['temperature night'] = pd.to_numeric(
    df['temperature night'], errors='coerce')

# Добавление в конец значения температуры в Фаренгейтах

fahrenheit_day = []
fahrenheit_night = []

for i in range(len(df)):
    fahrenheit_day.append(c_to_f(df.iloc[i]['temperature day']))
    fahrenheit_night.append(c_to_f(df.iloc[i]['temperature night']))


df['fahrenheit temperature day'] = fahrenheit_day
df['fahrenheit temperature night'] = fahrenheit_night

# статистическая информация

print(df['temperature day'].describe())
print(df['temperature night'].describe())

# фильтрация по температуре

# a = sort_by_temp(df, 23)
# print(a)

# фильтрация по двум датам (через datetime или через str)

# first_date = datetime.date(2010, 1, 5)
# second_date = datetime.date(2011, 6, 2)

# a = sort_by_date_1(df, first_date, second_date)
# print(a)

# first_date = '2010-01-05'
# second_date = '2011-06-02'

# b = sort_by_date_2(df, first_date, second_date)
# print(b)

# группировка по месяцу с вычислением среднего значения температуры
