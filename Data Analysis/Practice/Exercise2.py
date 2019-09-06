pimport pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"

users = pd.read_csv(url, sep = "|")
users.to_csv("jobs.csv")

#Here we are setting the user_id as index
users.set_index("user_id", inplace=True)

#print(users.head())

#Getting the first 25 entries
first_25 = users.head(25)

#Getting the last 10 entries
last_10 = users.tail(10)

#Counting the number of observations in the dataframe, the length
#There are various ways to do that
#The first

#users.shape returns a tuple which can be indexed [0] is rows and [1] is columns

#count() can be used but is much slower

#The ideal and fastest solution is to used is:
observations = len(users.index)

#Number of columns
col_num = len(users.columns)

#Column data types
types = users.dtypes

#Printing the occupation column
#print(users["occupation"])

occupations = users.drop_duplicates("occupation")
occupation_no = len(occupations.index)

#Summarizing the dataframe for the age column 
#This means describing it 
users.describe()

#Describing all the columns 
users.describe(include="all")

#Describing  only the occupation column
users["occupation"].describe()

mean = users["age"].mean()

#Finding the age with the least occurence 
#To get a DataFrame back, you have to apply a function to each group, 
#transform each element of a group, or filter the groups.

frequencies = users["age"].value_counts().to_dict()

uncommon_age = min(frequencies, key=frequencies.get)

print(observations)
print(col_num)
print(types)
print(occupation_no)
print(uncommon_age)
