# importing packages
import pandas as pd

# load json file using pandas
df1 = pd.read_json('all-keys.json')

# view data
print(df1)

# load json file using pandas
df2 = pd.read_json('verified-keys.json')

# view data
print(df2)

# use pandas.concat method 
df = pd.concat([df1,df2])

# view the concatenated dataframe
print(df)

# convert dataframe to csv file
df.to_csv("secret-scanner-results.csv",index=False)

# load the resultant csv file
result = pd.read_csv("secret-scanner-results.csv")

# and view the data
print(result)
