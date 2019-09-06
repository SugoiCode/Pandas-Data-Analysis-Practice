import pandas as pd 

# Create an example dataframe about a fictional army
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}

#Create dataframe from the dictionary
army = pd.DataFrame.from_dict(raw_data, orient = "columns")

#Set the origin column as the dataframe index
army.set_index("origin", inplace = True)

#Print the "vetarans" column
print(army["veterans"])

#Print the "veterans" and "deaths" columns
print(army[["veterans", "deaths"]])

#Print the name of all columns
#To avoid a list representation we can iterate over the list and print the names one by one
print(army.columns)

#Select the rows 3 to 7 and the columns 3 to 6
step_9 = army.iloc[2:6, 2:5]

#Select every row after the fourth row
step_10 = army.iloc[3:, :]

#Select every row up to the fourth
step_11 = army.iloc[:3, :]

#Select the 3rd column up to the 7th column
step_12 = army.iloc[:, 2:6]

#Select rows where deaths is greater than 50
step_13 = army[army["deaths"] > 50]

#Select rows where deaths is greater than 500 or less than 50
step_14 = army[(army["deaths"] > 500)  | (army["deaths"] < 50)]

#Select all the regiments not named Dragoons
step_15 = army[army["regiment"] != "Dragoons"]

#Select the rows called Texas and Arizona
step_16  = army.loc[ ["Texas", "Arizona"], :]

#Select the third cell in the row named Arizona
my_columns = list(army.columns)
step_17 = army.at[ "Arizona", my_columns[2] ]

#Select the third cell down in the column named deaths
step_18 = army.iloc[[2], army.columns.get_loc("deaths")]



