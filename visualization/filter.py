import pandas as pd

#converting csv to dataframe
d = pd.read_csv('visualization/criminal_data.csv')

#columns as options to choose from 
col = print("Options to checkout:")
print(pd.Series(d.columns))
choice1 = str(input("Enter the option you want to see results for:"))

#values of the selected column to choose from
print(f"Types of {choice1}:")
print(pd.Series(d[choice1].unique())) #distinct values
choice2 = str(input(f"Enter the {choice1} you want to check information for:"))

#dataframe with the records based on the respective values from the selected column
result_df = d.loc[(str(i).lower() == choice2.lower() for i in d[choice1])]
print(result_df)