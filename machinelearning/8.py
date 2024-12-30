#8. Calculate the cumulative sum of a NumPy array and store the results in a new Pandas DataFrame column. 
import pandas as pd 
import numpy as np 
data = {'Values': [100, 200, 300, 400, 500]} 
df = pd.DataFrame(data) 
numpy_array = np.array(df['Values']) 
df['Cumulative_Sum'] = np.cumsum(numpy_array) 
print(df) 
#output
'''   Values  Cumulative_Sum
0     100             100
1     200             300
2     300             600
3     400            1000
4     500            1500'''