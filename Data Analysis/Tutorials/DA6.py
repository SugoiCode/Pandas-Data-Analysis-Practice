#In this tutorial we will focus on modeling dataframes with pandas 
#After doing so we will feed such data to a machine learning algorithm 
#Workflow, data pre processing in pandas and then feed it to an ML algorithm
#Aim use past data on diamonds to predict future price
#Can we take all the properties of the diamond, feed to a regression model and predict the price of the diamond we are interested in

#First question: Are the characteristic descriptive enough to give us the price of our diamond
import pandas as pd 
import sklearn
from sklearn import svm, preprocessing

df = pd.read_csv("Datasets/diamonds.csv", index_col = 0) #We want to get rid of the index col, to avoid duplicating index column

#Anytime doing machine learning it is easy to cheat
#This means we shouldn't take too much info from the column that presents us with a solution
#All machine learning is linear algebra, therefore data must be in numerical values e.g. color, grade

df["cut"].unique() #Checking the grades of diamond which we want to convert into numerical information

"""
The following line of code (commented) will take the cuts column, find out how many uniques there are.
The assigns a code to our cut. 
As we are doing regression we would ideally want our numerical values to have a meaning.

"""

#df["cut"].astype("category").cat.codes

#We will instead create a dictionary which assigns a value in number to cut degree
#If the dictionary is large an automated way of creating it would be prefereable
#Due to the low amount of cuts we can just code in the value for every one of our degrees


cut_class_dict = {"Fair":1, "Good":2, "Very Good":3, "Premium":4, "Ideal":5}
clarity_dict = {"I3": 1, "I2": 2, "I1": 3, "SI2": 4, "SI1": 5, "VS2": 6, "VS1": 7, "VVS2": 8, "VVS1": 9, "IF": 10, "FL": 11}
color_dict = {"J": 1,"I": 2,"H": 3,"G": 4,"F": 5,"E": 6,"D": 7}

#Now we just want to map them
#This switch the keys with the values in the dataframe
df["cut"] = df["cut"].map(cut_class_dict)
df["clarity"] = df["clarity"].map(clarity_dict)
df["color"] = df["color"].map(color_dict)

#We now have our dataset which is now ready to be passed to a ML learning model

"""
We first want to shuffle our data. The reason is that the latest data may be more biased. 
Especially if the data in the model is sorted in any sort of way.
The current data set we are working on appears to be sorted by price.

In pandas there are many ways in which we can shuffle a dataframe. Can be done by index,
however that is considered to be ugly.
"""

df = sklearn.utils.shuffle(df)

#Now we want to assign values for x and y
#X are your features: list of features which point us to a label (input)
#Y is our label, what we want to predict (output)

x = df.drop("price", axis=1).values
X = preprocessing.scale(x) #Want to give our model something more digestible
y = df["price"].values

"""
Earlier on we discussed about cheating, if we currently print out our model. We can find out that we did 
not import the index which was present in the raw version of the data, we ensured this by making use of the index_col = 0,
as our data was originally sorted by price and index. We want to ensure that such information is not passed on onto our ML learning
algorithm.

It is extremely difficult to not fall for this error and it can happen all the time.
"""

#We now want to now split apart training and testing data
test_size = 200

#Data we will fit against. Training Data
x_train = x[:-test_size] #train up to the last 200
y_train = y[:-test_size]

#Data we will use to test our model
x_test =  x[-test_size]
y_test =  y[-test_size]

clf = svm.SVR(kernel="linear") #clf stands for classifier
clf.fit(x_train, y_train)

print(clf.score(x_test, y_test))


