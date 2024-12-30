#4. Select the first and last 7 rows of a Pandas DataFrame. 
import pandas as pd 
data = {'Name': ['Serij', 'Ram', 'Rabin', 'Santosh', 'Milan', 'Alina', 'Bijay', 'Chandra', 'Dinesh', 
'Suman'], 
'Age': [26, 32, 25, 31, 28, 22, 35, 30, 40, 28], 
'Salary': [50000, 60000, 45000, 70000, 55000, 60000, 70000, 55000, 75000, 65000]} 
df = pd.DataFrame(data) 
selected_rows = pd.concat([df.head(7)]) 
print("First 7 rows:") 
print(selected_rows) 
selected_rows = pd.concat([df.tail(7)]) 
print("\nLast 7 rows:") 
print(selected_rows) 
#output
'''First 7 rows:
      Name  Age  Salary
0    Serij   26   50000
1      Ram   32   60000
2    Rabin   25   45000
3  Santosh   31   70000
4    Milan   28   55000
5    Alina   22   60000
6    Bijay   35   70000

Last 7 rows:
      Name  Age  Salary
3  Santosh   31   70000
4    Milan   28   55000
5    Alina   22   60000
6    Bijay   35   70000
7  Chandra   30   55000
8   Dinesh   40   75000
9    Suman   28   65000'''