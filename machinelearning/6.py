#6. Extract rows from a Pandas DataFrame where a specific column's values are in a given NumPy array. 
import pandas as pd 
import numpy as np 
data = {'Name': ['Teodosija', 'Sutton', 'Taneli', 'David', 'Emily'], 
'Age': [25, 30, 22, 35, 28], 
'Salary': [50000, 60000, 45000, 70000, 55000]} 
df = pd.DataFrame(data) 
selected_age_values = np.array([25, 35]) 
selected_rows = df[df['Age'].isin(selected_age_values)] 
print(selected_rows) 
#output
'''        Name  Age  Salary
0  Teodosija   25   50000
3      David   35   70000'''