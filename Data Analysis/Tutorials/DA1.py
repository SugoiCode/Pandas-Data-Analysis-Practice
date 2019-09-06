import pandas as pd
import matplotlib.pyplot as plt

"""
Pandas deal with objects which have rows and columns.
Excel, csv and many more. Once you deal with your object you can push out the data
in a different format.
"""

#Defining a dataframe(df), the object which is our columns and rows
#Series is just a single column
#Panel is multiple dataframes, columns rows and depth
df = pd. read_csv("Datasets/avocado.csv")

df.head() #Prints the first N rows of our dataframe. Default is five but we can set the argument with a different number

df.tail() #Prints the last N rows of our dataframe, works the same way as head

#If you want to reference a specific column, indexing
#Add head to print the first 5 rows of the columns we are referencing
 
df['AveragePrice'].head()

#We can specify regions in our avocado dataframe
#We therefore create a new dataframe which matches our requirements
#The section of the main dataframe where the df['region'] (our column) is equal to Albany
albany_df = df[df['region'] == "Albany"]
albany_df.head() #Gets the first five columns of our new dataframe made up of only Albany regions

#Dataframes have indexes in their first columns
albany_df.index # will give the indexes of all the rows in our dataframe (usually meaningless)

#In our avocado dataframe we want the Date to be our meaningful index
albany_df.set_index("Date")

albany_df.head() #We lost the date, this is because pandas operations usually return a new dataframe

#Therefore when dealing with pandas we have two options of how to deal with things
#inplace for some of the commands whilst other do not have an options

#albany_df = albany_df.set_index("Date") #We simply reassigned to a new dataframe 
#Otherwise
#If both are used error occurs as we are resetting the index twice the same way because the key no longer exists, it is now an index.
albany_df.set_index("Date", inplace=True) #will modify albany_df in place hence no need to reassign things

#The next step is to allow graphing of data
albany_df.plot()

#or plot specific columns
albany_df['AveragePrice'].plot()

plt.show() #will display all the data which was plotted.


