import pandas as p

df = p.read_csv('data.csv', sep=';')
# for index, row in df.iterrows():
#     print(df['url'][index])

print(df['title'][1])