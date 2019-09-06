import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"

#data presents errors so will use additional parameter to eliminate offending lines
chipo = pd.read_csv(url, sep = "\t")

menu = chipo.drop_duplicates(subset = ["quantity", "item_name"])
menu.sort_values("item_price", ascending = False, inplace=True)
menu = menu[menu["quantity"] == 1]
#print(chipo.head())

#Creating a new dataframe called info with only price and name of item
info = chipo[["item_price", "item_name"]]

#Sorting item in  vc by name
chipo.sort_values("item_name", inplace=True)

#Checking price column type
#Eliminating the dollar sign from the string, subsequently converting the string to a numerical value
#This is so we can find the largest price in the list
chipo["item_price"] = chipo["item_price"].str.replace('$','' )
chipo["item_price"] = pd.to_numeric(chipo["item_price"])

#Creating a new dataframe containg only the highest prices
pricy = chipo[chipo["item_price"] == chipo["item_price"].max()]

pricy_quantity = pricy["quantity"].max()

#Finding how many veggie salad bowls were ordered
#Counting how many times all the values in the dictionary repeat and converting to a dictionary for future access
#To improve
frequencies = chipo["item_name"].value_counts().to_dict()

#Number of times veggie bowl gets 
veg_bowl_freq = frequencies["Veggie Salad Bowl"]

#Finding how many times people order more than one canned soda
more_soda = chipo[(chipo["item_name"] == "Canned Soda") & (chipo["quantity"] > 1)].count()

print(pricy, "\n")
print(pricy_quantity, "\n")
print(veg_bowl_freq, "\n")
print(more_soda, "\n")
print(menu.head(10))