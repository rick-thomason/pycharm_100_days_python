# with open('weather_data.csv') as weather_data:
#     data = [data.strip() for data in weather_data]
#     for weather in data[1:]:
#         day_of_week = weather.split(',')[0]
#         temp = weather.split(',')[1]
#         condition = weather.split(',')[-1]
#         print(f'On {day_of_week}, it was {temp}C and {condition}.')

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#
#     temperatures = []
#     for row in list(data)[1:]:
#         temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

data = pd.read_csv('weather_data.csv')
# print(data)
# print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)

data_list = data['temp'].to_list()
# print(data_list)

# print(data['temp'].mean().round(2))
# print(data['temp'].max())

# create dataframe from scratch
data_dict = {
    'students': ['Rick', 'Maddox', 'Roland'],
    'scores': [77, 88, 99]
}

df = pd.DataFrame(data_dict)
print(df)

df.to_csv('scores.csv')