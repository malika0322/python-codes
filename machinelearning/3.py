#3. Select rows from a DataFrame based on multiple conditions. 
import pandas as pd 
data = {'Name': ['Serij', 'Ram', 'Rabin', 'Santosh', 'Milan'], 
'Age': [26, 32, 25, 31, 28], 
'Salary': [50000, 60000, 45000, 70000, 55000]} 
df = pd.DataFrame(data) 
selected_rows = df[(df['Age'] > 25) & (df['Salary'] > 50000)] 
print(selected_rows) 
#output
'''      Name  Age  Salary
1      Ram   32   60000
3  Santosh   31   70000
4    Milan   28   55000'''