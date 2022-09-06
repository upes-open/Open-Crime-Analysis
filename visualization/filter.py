import pandas as pd

d = pd.read_csv('visualization/criminal_data.csv')
print("Types of Crime:")
print(pd.Series(d['Crimes'].unique()))
c = str(input("Enter the incident you want to check:")).lower()
result_df = d.loc[(i.lower() == c.lower() for i in d['Crimes'])]
print(result_df)