import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt

"""
In this next section we will focus on visualizing that correlation table 
which we worked on in the last tutorial.
"""

df = pd.read_csv("Datasets/minwage.csv")

act_min_wage = pd.DataFrame()

for name, group in df.groupby("State"):
	if act_min_wage.empty:
		act_min_wage = group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name})
	else:
		act_min_wage = act_min_wage.join(group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name}))
	
min_wage_corr = act_min_wage.replace(0, np.NaN).dropna(axis=1).corr()

#With the above code we have constructed our correlation table. We not want to graph it
plt.matshow(min_wage_corr)
plt.show()
plt.close()

#We are now going to make us of matplotlib to enable better and easier visualization of the data at hand. There is another tutorial for such

#The labels being numbers do not help with visualization
#We therefore make a list commprehension
labels = [c[:2] for c in min_wage_corr.columns]#

fig = plt.figure(figsize = (12, 12))

#This is fine if the aim is to plot a DataFrame, if we want to modify things due to the nature of 
#matplot lib a fiture is required

ax = fig.add_subplot(111) # This means this is number one of a 1 by 1 grid

ax.matshow(min_wage_corr, cmap = plt.cm.RdYlGn)#red yellow green


#Matplot lib doesn't put all the labels available and limits the amounts
ax.set_xticks(np.arange(len(labels)))
ax.set_yticks(np.arange(len(labels)))

ax.set_yticklabels(labels) #Setting labels
ax.set_xticklabels(labels)

#Requests allo  ws us to make us ofg smarter ways to access the internet
web = requests.get("https://www.infoplease.com/state-abbreviations-and-state-postal-codes")

#We need to map the statename to a 2 letter abbreviation system
dfs = pd.read_html(web.text) #Parses a website and returns a list of all the dataframes found in website no matter the amounts 


for df in dfs:
	print(df.head()) #We check the dataframes
	
#We have found out that the the dataframe with the state name abbreviations is the first one
state_abbv = dfs[0] #access dataframes since the dataframes are stored in a list
state_abbv.head()

#To avoid making continuous requests to the website, we now store the dataframe to a csv
state_abbv.to_csv("Datasets/state_abbv.csv ", index = False)
#By adding such the index data will not be saved
"""
NOTE: 
Pandas believes our index is meaningful,  therefore when saving to a CSV file
the CSV doesn't understand anything is an index. Therefore it will assume we want to save 
the index.
"""

#We will now read it back in
state_abbv = pd.read_csv("Datasets/state_abbv.csv", index_col = 0) 
state_abbv.head() #As we can notice we now have 2 index columns
#If we continue such behavior of saving and reloading the number of index columns will keep getting larger
#Instead we can add index_col= 0 in the parameters

abbv_dict = state_abbv[["Postal Code"]].to_dict()

abbv_dict = abbv_dict["Postal Code"] #We now have a dictionary that we can easily map to a column  

abbv_dict["Federal (FLSA)"] = "FLSA"
abbv_dict["Guam"] = "GU"
abbv_dict["Puerto Rico"] = "PR"
labels = [abbv_dict[c] for c in min_wage_corr.columns]