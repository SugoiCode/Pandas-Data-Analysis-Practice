import pandas as pd
import numpy as np

#importing csv file from web link
euro12 = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv", sep = ",")

#Selecting the Goal column
goal = euro12["Goals"]

#Finding out how many teams participated in the Euro2012
team_no = len(euro12["Team"])

#Number of columns in the dataset
col_no = len(euro12.columns)

#Creating a new dataframe called Discipline
discipline = euro12[ ["Team", "Yellow Cards", "Red Cards"] ]

#Sorting out new teams by red and yellow cards
by_red = discipline.sort_values("Red Cards")

by_yellow = discipline.sort_values("Yellow Cards")

#Calculating the mean yellow cards given per Team
mean_yellow = discipline["Yellow Cards"].mean()

#Filtering teams that scored more than 6 goals
six_or_more = euro12[euro12["Goals"] > 6]

#Selecting teams that start with a G
g_start = euro12[euro12["Team"].str.startswith("G") == True]

#Selecting the first n columns
#We have to index the columns but not knowing the column length
#We can col_no for guidance
first_seven_cols = euro12.iloc[:, [0,2] ]
 
#Select all columns except the last seven
except_3 = euro12.iloc[:, [0, (col_no - 4)]]

#Shooting Accuracy  from England, Italy and Russia
countries = ["Englad", "Italy", "Russia"]
#egi_accuracy = euro12["Shooting Accuracy"[euro12["Team"] in countries]]
#The model answers resultm isin takes a list as an argument
#England is not displayed as it may have been previously cleaned out. When I try to locate it, it gives off a KeyError
egi_accuracy = euro12.loc[euro12.Team.isin(countries), ["Team", "Shooting Accuracy"]]




print(goal.head())
print(team_no)
print(col_no)
print(discipline.head())
print(mean_yellow)
print(six_or_more.head())
print(g_start.head())
print(egi_accuracy)
print()