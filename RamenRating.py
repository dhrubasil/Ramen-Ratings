# importng all the important packages
from typing import Any, Union

import numpy as np  #Linear Algebra
import pandas as pd  #Data Processing
import matplotlib.pyplot as plt  #Data Visualization
import seaborn as sns  #Data Visaulization

data = pd.read_csv('ramen-ratings.csv')  #Reading the data

#data.head(10) #Show the first 10 row of dataset
#print(data.head(10)) #Print
#print(data.shape) #Checking the number of Rows and column
#print(data.isna().sum()) #print

data = data.dropna(subset=['Style'])

#print(data['Style'].isna().sum()) #print
#print(data['Style'].unique()) #print
#print(data['Style'].value_counts()) #print
#print(data['Country'].unique())
#print(len(data['Country'].unique()), 'Countries')
#print(data['Country'].value_counts())

top10 = data.dropna()
#print(top10)

top10 = top10[top10['Top Ten'] != '\n'] #if the data in Top Ten column contains '\n' we can ignore it
top10 = top10.sort_values('Top Ten' ) #and we sort it by year
#print(top10)

#print(data['Brand'].value_counts()[:10])

#First, let's see how many ramen brands are in our data
#print(len(data['Brand'].unique()))

for s in data['Stars']:
    try:
        s = float(s)
    except:
        print(s)

data = data[data['Stars'] != 'Unrated']
#print(data[data['Stars'] == 'Unrated']['Stars'].sum()) #make sure if there are no 'Unrated'

brands = list(data['Brand'].unique())
counter = [0.0]*355

brands_cnt = dict(zip(brands, counter)) #create dictionary to count all ratings and then save the averages

for brand in brands:
    brands_data = data[data['Brand'] == brand]
    for star in brands_data['Stars']:
        brands_cnt[brand] += float(star) #count all ratings
    brands_cnt[brand] /= len(brands_data) #average

top50ratings = [] #list for saving the brand name and its average rating
for key, values in brands_cnt.items():
    top50ratings.append([key,values])

#print the top 50 ramen ratings by brand
top50ratings = sorted(top50ratings, key = lambda x : x[1], reverse = True) #sorting values in descending order
#print(top50ratings)

#for i in range(50):
    #print('#{:<3}{:25} {}'.format(i+1, top50ratings[i][0], round(top50ratings[i][1],2)))

sns.set(style = 'darkgrid')
f, ax = plt.subplots(1,1,figsize = (15,5))
sns.countplot(x = 'Country', data = data)
plt.xticks(rotation=90)

#plt.show()

labels = 'Pack', 'Bowl', 'Cup' , 'Tray', 'Box' #We can't include 'Bar' and 'Can' because they only appear once in our data.
size = [1531, 481, 450, 108, 6]

f, ax = plt.subplots(1,1, figsize= (10,10))

ax.pie(size, labels = labels, autopct = '%1.2f%%', startangle = 180)
ax.axis('equal')
ax.set_title("Style", size = 20)

plt.show()