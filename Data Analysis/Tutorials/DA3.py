import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
This tutorial does something similar to the previous tutorial in the sense that it creates a new 
dataframe where the columns are the states and then each row will be contains the average for the 
change in wage. These will then be plotted together on the same graph in order to allows us to compare
the changes
"""

df = pd.read_csv("Datasets/MinWage.csv", encoding = "latin")
#When reading the file we get an error in format as pandas prefers a utf-8 format
#Usually we would make use of "utf8" in the encoding parameter
#If there is an encoding issue the latin parameter usually solves it

#We now save this avoid any future problems
#By adding the index=False to the arguments we are able to avoid dealing with an unnamed column
df.to_csv("Datasets/minwage.csv", encoding="utf-8")

df = pd.read_csv("Datasets/minwage.csv")

#The aim here is to make a new dataframe in which the states are the rows

gb = df.groupby("State") #Allows us to create this group by object
gb.get_group("Alabama").set_index("Year").head()

#This returns the portion of dataframe which in which the State columns corresponds to Alabama


#We are now creating a new dataframe in which the columns correspond to the States and the rows correspond to the year
act_min_wage = pd.DataFrame()

for name, group in df.groupby("State"): #This is the same as the last tutorial however we instead use  the tools offered by pandas rather than straight python logic which is much faster
	#in group by we get the name and then the group which will be our dataframe
	if act_min_wage.empty:
		act_min_wage = group.set_index("Year")[["Low.2018"]].rename(columns = {"Low.2018":name})
		#In the above line of code if the dataframe is empty we first create a new dataframe
		#Set which column will serve as th e index and then rename the columns with the state
	else:
		act_min_wage = act_min_wage.join(group.set_index("Year")[["Low.2018"]].rename(columns = {"Low.2018":name}))
		
#print(act_min_wage.head())

#describe() will give us information regarding our data for each row which can be used
print(act_min_wage.describe())

#Pandas also allows correlation and covariance to be done very quickly for us
act_min_wage.corr()

#As we can see in our data Alabama doesn't have any values initially
issue_df = df[df['Low.2018']==0] #We create a new dataframe to check where our Low.2018 values are 0

#To view all the state which have a 0 value for Low.2018 we can create a list with them as such:
issue_df['State'].unique() #This will return a list with all the states in the dataframe

#Since the data is missing and no good for the state in the issue_df datasets we can eliminate them as the data is useless
min_wage_corr = act_min_wage.replace(0, np.NaN).dropna(axis=1).corr().head()#we replace all the 0 values with NaN and drop them
#When axis = 1 we delete a column if the data is NaN, default is usually 0 which signifies the rows
#We have now returned the states that have minimum wage data

for problem in issue_df['State'].unique():
	if problem in min_wage_corr.columns:
		print("Something is missing here")

grouped_issues = issues_df.groupby("State")

grouped_issues.get_group("Alabama").head(3)

#We expect the entire column to add up to zero because we never get minimum wage data for Alabama
grouped_issues.get_group("Alabama")['Low.2018'].sum()

#In much the same fashion we can check for all the States
for state, data in grouped.issues:
	if data['Low.2018'].sum() != 0:
		print("We missed something!")