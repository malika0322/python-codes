#5. Merge two Pandas DataFrames based on a common column. 
import pandas as pd 
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Rabin', 'Santosh', 'Milan']}) 
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Age': [25, 30, 22]}) 
merged_df = pd.merge(df1, df2, on='ID') 
print(merged_df)
#output
'''   ID     Name  Age
0   2  Santosh   25
1   3    Milan   30'''