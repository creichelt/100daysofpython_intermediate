# with open('weather_data.csv') as file:
#     date = file.readlines()
#
#     print(data)


# import csv
#
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas as pd

# data = pd.read_csv('weather_data.csv')
# print(data['temp'].max())
# print(data.temp.mean())
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == 'Monday']
# print(monday.condition)
# print(monday.temp)
# tempmonday_temp_f = int(monday.temp) *9/5 + 32
# print(monday_temp_f)

# create DataFrame from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
#
# df = pd.DataFrame(data_dict)
# df.to_csv('new_data.csv')

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

fur = 'Primary Fur Color'
# ct = data[fur].value_counts()
# print(ct)
# ct.to_csv('new_fur.csv')

grey_squirrels_count = len(data[data[fur] == 'Gray'])
red_squirrels_count = len(data[data[fur] == 'Cinnamon'])
black_squirrels_count = len(data[data[fur] == 'Black'])

data_dict = {
    'Fur Color': ['Gray', ' Cinnamon', 'Black'],
    'Count': [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')