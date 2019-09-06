import pandas as pd

#GroupBy summarises as Split-Apply-Combine
#Split the data, apply functions on it and then recombine the data

#Reading the csv file 
drinks = pd.read_csv("Datasets\drinks", index_col = 0)

#Finding the country with the highest beer servings
step_4 = drinks["country"][drinks.beer_servings == drinks.beer_servings.max()] 

#Displaying the country and its relative wine servings
step_5 = drinks[["country", "wine_servings"]]

#Finding the mean for the three drink types
step_6 = drinks[["beer_servings", "spirit_servings", "wine_servings"]].mean()

#Finding the median for the three drink types
step_7 = drinks[["beer_servings", "spirit_servings", "wine_servings"]].median

#Getting the mean, min and max values for spirit consumption and then output to a Dataframe
minimum = drinks["spirit_servings"].min()

maximum = drinks["spirit_servings"].max()

mean = drinks["spirit_servings"].mean()

#When passing scalar values to the creation of a dataframe if the values are scalar
#They should be passed as lists or pass an index such as [0]

statistics = {
					'min_spirits_servings': [minimum],
					'max_spirits_servings': [maximum],
					'mean_spirits_servings': [mean]
					}
					
stats_dataframe = pd.DataFrame.from_dict(statistics, orient = "columns")

"""
Due to the difficulty of the exercise here are model answers. 
To use for inspiration. 
"""

#In this answer we have to find which country drinks more beer on average
#Therefore we make use of groupby to select 
answer_4 = drinks.groupby("continent").beer_servings.mean()

#Print statics for each continent related to wine consumption
drinks.groupby("continent").wine_servings.describe()

#Print the median alcohol consumption per continent for every column
drinks.groupby("continent").median()

#Print the mean, min and max values for spirit consumption
drinks.groupby("continent").spirit_servings.agg(["mean", "min", "max"])

