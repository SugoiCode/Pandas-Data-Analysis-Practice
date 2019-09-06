import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Datasets/avocado.csv")
df['Date'] = pd.to_datetime(df["Date"])


#albany_df = df[df["region"] == "Albany"]
#albany_df.set_index("Date", inplace=True)
#albany_df["AveragePrice"].plot()
#plt.close()  # Avoids plotting it again once we are done with it.

#As seen in the graph representations the dates run over each other
#This means pandas doesn't realize we are dealing with dates
#Therefore convert that to a date time to_datetime()
#Now to smoothen the dataout and look easier to handle we use a rolling-point average

#albany_df['AveragePrice'].rolling(25).mean().plot()
#plt.close()
#As we can see from the plot and the analysis the dates aren't in proper chronological order
#Therefore
#albany_df.sort_index(inplace=True) #We can also sort dataframes by columns which will also adjust the index
#albany_df['AveragePrice'].rolling(25).mean().plot()

#plt.show()
#plt.close()

#Since the operation we made smoothened out our data, we will create a new columns in our dataframe with it
#albany_df['price25ma'] = albany_df['AveragePrice'].rolling(25).mean() 

#albany_df.head(3) #There price25ma gives us NaN, this is because the rolling periods require 25 days to be calculated. Hence first 25 will be NaN
#Otherwise
#albany_df.tail(3) #Won't present NaN values

#albany_df.dropna().head(3) #Dropna removes any rows which contain NaN values, head will display the head of the new dataframe

"""
When doing operations on a dataframe and fork the original dataframe and then fork into another dataframe (albany_df)
we shouldn't forget that such dataframe came from the original one therefore value changes could be occurring in a different way
from intended.

To avoid the warnings from pandas we should notify on the fact that we are aware of the fact that we are working on a copy of the original dataframe.
"""

#We do this by saying
#albany_df = df.copy() #This returns to us a new copy of the dataframe and it won't impact albany_df



#When copying we can immediately treat the copy as a new dataframe therefore we could also do:
albany_df = df.copy()[df["region"] == "Albany"] #New dataframes made of only rows in which the region is Albany
#We can now perform our standard operations without any warnings
albany_df.set_index("Date", inplace=True)
albany_df.sort_index(inplace=True)
albany_df['price25ma'] = albany_df['AveragePrice'].rolling(25).mean()
#Now we have no warnings

#Suppose we want to draw all the regions and compare them
#We need to figure out all the regions, therefore we need to iterate over the regions
#We can iterate over the regions as each column can be treated as an array
#Thus allowing us to treat a dataframe as a multidimensional array, each columns can be treated as an array

df.values # returns a multidimensional array comprised of the columns

list(set(df['region'].values.tolist())) #Will give us an array which can be converted to a list with the to_list command, to get unique items we convert to a a set and then back to a list

#This code is messy and bad practice, therefore to do that we make use of
df['region'].unique() #This allows to get all the unique values and then iterate over it

"""
TIP: Look through the panda docs as the operations in there are optimised and will be faster than the python version which is often messy
"""

"""
On matplot lib we have a canvas in the background and we can plot over and over.
Ideally to be more efficient we can create a new dataframe, reshaped where the column headers are the regions
and the values of those columns are the rolling average and the date.
"""

"""
graph_df  =pd.DataFrame()

for region in df['region'].unique()[:16]:
	print(region)
	region_df = df.copy()[df['region'] == region]
	region_df.set_index("Date", inplace=True)
	region_df.sort_index(inplace=True)
	region_df[f'{region}_price25ma'] = region_df['AveragePrice'].rolling(25).mean() #The regions all have the same column name f'{region}_price25ma' assigns a new name to each region
	
	if graph_df.empty:
		graph_df = region_df[[f'{region}_price25ma']] #this will create a series therefore double brackets to have a dataframe
	else:
		graph_df = graph_df.join(region_df[f'{region}_price25ma']) #This allows us to join the dataframes to be joined into 1 dataframe

df['type'].unique() #We find out there are 2 types therefore we need to select either of the types
"""
#We therefore have to pick a type as so:

df2 = pd.read_csv("Datasets/avocado.csv")
df2 = df2.copy()[df2['type'] == "organic"]
df2['Date'] = pd.to_datetime(df2["Date"])

df2.sort_values(by="Date", ascending=True, inplace=True) #Here we sort a dataframe by values rather than index


graph_df2  = pd.DataFrame()

for region in df2['region'].unique()[:16]:
	#print(region)
	region_df2 = df2.copy()[df2['region'] == region]
	region_df2.set_index("Date", inplace=True)
	region_df2.sort_index(inplace=True)
	region_df2[f'{region}_price25ma'] = region_df2['AveragePrice'].rolling(25).mean() #The regions all have the same column name f'{region}_price25ma' assigns a new name to each region
	
	if graph_df2.empty:
		graph_df2 = region_df2[[f'{region}_price25ma']] #this will create a series therefore double brackets to have a dataframe
	else:
		graph_df2 = graph_df2.join(region_df2[f'{region}_price25ma']) #This allows us to join the dataframes to be joined into 1 dataframe

df['type'].unique() #We find out there are 2 types therefore we need to select either of the types

graph_df2.dropna().plot(figsize=(8,5), legend=False)
plt.show()
#The graph plots correctly however the legend is too large and the graph size is to small to give an accurate representations
#Pandas allows us to use matplotlib to create better custom charts due to pandas importation ability
#If we look at the graph the beginning of the graph is empty, this is due to NaN values, therefore as the above code shows we can drop these values