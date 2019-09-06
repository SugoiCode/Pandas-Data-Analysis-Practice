import pandas as pd
import numpy as np

#Reading in the dataframe saved previously
chipo = pd.read_csv("Datasets\chipo.csv", index_col = 0)

#Cleaning the price column to a float#
chipo["item_price"] = chipo["item_price"].str.replace('$','' )
chipo["item_price"] = pd.to_numeric(chipo["item_price"])

#Creating a new dataframe which hhas only the item and the price
info = chipo[["item_name", "item_price"]].drop_duplicates()

#Sorting out the original dataframe by item name
chipo.sort_values("item_name", ascending = True, inplace=True)


#Creating a new dataframe containg only the highest prices
pricy = chipo[chipo["item_price"] == chipo["item_price"].max()]

#Finding out the quantity
pricy_quantity = pricy["quantity"].max()

#Veggie bowl salad
frequencies = chipo[ "item_name" ].value_counts().to_dict()

veggie_bowl = frequencies["Veggie Salad Bowl"]

#Finding how many times people order more than one canned soda
more_soda = chipo[(chipo["item_name"] == "Canned Soda") & (chipo["quantity"] > 1)].count()
