import pandas as pd
import csv
import os


def c_to_f(temperature: int) -> int or str:
    """Конвертирует температуру в градусах Цельсия в градусы Фаренгейта

    Args:
        temperature (int): Значение температуры в Цельсиях

    Returns:
        int or str: Возвращаемое значение в Фаренгейтах , либо строку 'None'
    """
    if temperature == 'None':
        return 'None' 

    return (int(temperature) * 9/5) + 32


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

# обработка пропущенных значений

for i in range(len(df)):

    if df.iloc[i]['date'] == '':
        df.iloc[i]['date'] = 'None'

    if df.iloc[i]['temperature day'] == '':
        df.iloc[i]['temperature day'] = 'None'

    if df.iloc[i]['pressure day'] == '':
        df.iloc[i]['pressure day'] = 'None'

    if df.iloc[i]['wind day'] == '':
        df.iloc[i]['wind day'] = 'None'

    if df.iloc[i]['temperature night'] == '':
        df.iloc[i]['temperature night'] = 'None'

    if df.iloc[i]['pressure night'] == '':
        df.iloc[i]['pressure night'] = 'None'

    if df.iloc[i]['wind night'] == '':
        df.iloc[i]['wind night'] = 'None'

# Добавление в конец значения температуры в Фаренгейтах

fahrenheit_day = []
fahrenheit_night = []

for i in range(len(df)):
    fahrenheit_day.append(c_to_f(df.iloc[i]['temperature day']))
    fahrenheit_night.append(c_to_f(df.iloc[i]['temperature night']))


df['fahrenheit temperature day'] = fahrenheit_day
df['fahrenheit temperature night'] = fahrenheit_night

print(df)