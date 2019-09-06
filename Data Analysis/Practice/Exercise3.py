import pandas as pd
import numpy as np 

food  = pd.read_csv("Datasets\en.openfoodfacts.org.products.tsv", sep = "\t")

first_5 = food.head()

observations = len(food.index)

col_no = len(food.columns)

food.columns

#or iterate over the list returned by .columns with a for loop

#There are two ways to access the 105th column 
#We can use either loc or iloc
#loc allows us to locate using the row's index name(as indexes may not always be numerical) and the column's name
#iloc instead allows us to use the dataframe's index(the actual name)
#In this case I just want to retrieve the column's name which I can simply do by doing:
col_name_105 = food.columns[104]

#this is the column's type
col_type_105 = food[col_name_105].dtypes

#How the data set it indexed
how_index = food.index

#Product name of the 19th observations #Actual answer food.values[18][7] meaning we can find the index of the column name and access the cell value through indexing 
row_19 = food.values[18][7]

print(how_index)
print(col_name_150)
print(col_type_150)
print(row_19)