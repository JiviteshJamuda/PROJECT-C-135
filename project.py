import pandas as pd
import csv
import matplotlib.pyplot as plt

df = pd.read_csv('filtering_stars.csv')
df.drop(['Unnamed: 0','Unnamed: 0.1' ], axis = 1, inplace = True)
# print(df.head(10))
# print(df.shape)

name = df['name'].tolist()
distance = df['distance'].tolist()
mass = df['mass'].tolist()
radius = df['radius'].tolist()
gravity = df['gravity'].tolist()
# print(name)

plt.figure(figsize = (10,5))
plt.title('mass')
plt.bar(name[0:9], mass[0:9])
plt.show()

plt.figure(figsize = (10,5))
plt.title('radius')
plt.bar(name[0:9], radius[0:9])
plt.show()

plt.figure(figsize = (10,5))
plt.title('distance')
plt.bar(name[0:9], distance[0:9])
plt.show()

plt.figure(figsize = (10,5))
plt.title('gravity')
plt.bar(name[0:9], gravity[0:9])
plt.show()