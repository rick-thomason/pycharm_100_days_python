import pandas as pd

df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
df.columns = [x.replace(' ', '_') for x in df.columns]
df.columns = [x.lower() for x in df.columns]


fur_color_count = df['primary_fur_color'].value_counts()
# print(fur_color_count)

squirrel_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [2473, 392, 103]
}

squirrel_count = pd.DataFrame(squirrel_dict)
squirrel_count.to_csv('squirrel_count')