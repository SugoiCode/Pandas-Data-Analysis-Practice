import pandas as pd 

url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"

occupation = pd.read_csv(url, sep = "\t")

occupation.to_csv("Datasets\occupation.csv")