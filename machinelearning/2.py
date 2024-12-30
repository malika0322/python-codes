#2. Create a DataFrame from a NumPy array with custom column names. 
import pandas as pd 
import numpy as np 
numpy_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) 
column_names = ['Column1', 'Column2', 'Column3'] 
df = pd.DataFrame(data=numpy_array, columns=column_names) 
print(df) 
#output
'''   Column1  Column2  Column3
0        1        2        3
1        4        5        6
2        7        8        9'''