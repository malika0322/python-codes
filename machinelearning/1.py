#1. Load a CSV file into a Pandas DataFrame. 
import pandas as pd 
file_path = 'test.csv' 
df = pd.read_csv(file_path) 
print(df) 
#output
'''    name  age         city
0  Alice   30     New York
1    Bob   25  Los Angeles'''