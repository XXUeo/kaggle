import csv as csv
import numpy as np
import pandas as pd
import pylab as P

# csv_file_object = csv.reader(open('csv/train.csv', 'rb')) 
# header = csv_file_object.next() 
# data=[] 

# for row in csv_file_object:
#     data.append(row)
# data = np.array(data) 


# ages_onboard = data[0::,5].astype(np.float) 
# print ages_onboard

df = pd.read_csv('csv/train.csv', header=0)
#print df

#this is for datatypes
#print df.dtypes

#basic data info
#print df.info()
#print df.describe()
#this is so coolll@!!!!!

#selected data
#print df.Age[0:10]


#print type(df['Age'])
#this is for kind of object

#print df['Age'].mean()
#print df['Age'].median()

#print df[ ['Sex', 'Pclass', 'Age'] ]
#print df[df['Age'] > 60]
#print df[df['Age'].isnull()][['Sex', 'Pclass', 'Age']]

# this is for histgram
# for i in range(1,4):
#     print i, len(df[ (df['Sex'] == 'male') & (df['Pclass'] == i) ])
# df['Age'].hist()
# P.show()



df['Age'].dropna().hist(bins=16, range=(0,80), alpha = .5)
P.show()







