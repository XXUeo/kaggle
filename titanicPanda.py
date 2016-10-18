import csv as csv
import numpy as np
import pandas as pd
import pylab as P

# Import the random forest package
from sklearn.ensemble import RandomForestClassifier 







# csv_file_object = csv.reader(open('csv/train.csv', 'rb')) 
# header = csv_file_object.next() 
# data=[] 

# for row in csv_file_object:
#     data.append(row)
# data = np.array(data) 


# ages_onboard = data[0::,5].astype(np.float) 
# print ages_onboard

df = pd.read_csv('csv/train.csv', header=0)
data = df
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



#df['Age'].dropna().hist(bins=16, range=(0,80), alpha = .5)
#P.show()








###########Clearning the data


df['Gender'] = 4
df['Gender'] = df['Sex'].map( lambda x: x[0].upper() )
#Iambda x is an built-in function of python for generating 
#an anonymous function in the moment, at runtime.
# Remember that x[0] of any string returns its first character.
df['Gender'] = df['Sex'].map( {'female': 0, 'male': 1} ).astype(int)
#changing female = 0 male = 1

#print df['Gender']







#now create 2d array. row = gender column = Pclass

median_ages = np.zeros((2,3))
#print median_ages
#zero array

for i in range(0,2):
	for j in range(0,3):
		median_ages[i,j] = df[(df['Gender'] == i) & \
                              (df['Pclass'] == j+1)]['Age'].dropna().median()
#we get median of ages for each gender and pclass.

#print median_ages


df['AgeFill'] = df['Age']

df.head() # head in default displays 5

#so it's displaying each where Age = null. AgeFill is added as same as Age
#print df[ df['Age'].isnull() ][['Gender','Pclass','Age','AgeFill']].head(10)




#now put null to Age, and filling AgeFill
for i in range(0, 2):
    for j in range(0, 3):
        df.loc[ (df.Age.isnull()) & (df.Gender == i) & (df.Pclass == j+1),\
                'AgeFill'] = median_ages[i,j]


#tara--
#print df[ df['Age'].isnull() ][['Gender','Pclass','Age','AgeFill']].head(10)


#this is a checker wether (Age=Null) = (Age= nonNull)
df['AgeIsNull'] = pd.isnull(df.Age).astype(int)


#parch = number of parents or children
#SibSp = number of siblings or spouse
df['FamilySize'] = df['SibSp'] + df['Parch']
df['Age*Class'] = df.AgeFill * df.Pclass

df['FamilySize'].hist()
df['Age*Class'].hist()
#P.show()










#final preparation



#print df.dtypes

#print df.dtypes[df.dtypes.map(lambda x: x=='object')]

df = df.drop(['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1) 
df = df.drop(['Age'], axis=1)
#print df


# df = df.dropna()
#this one drop any rows which still have missing values

# we just have coverted into numPy array
train_data = df.values


#compare these two!!
print (train_data)
print (data)













