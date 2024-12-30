#10.  Perform matrix multiplication using NumPy. 
import numpy as np 
matrix1 = np.array([[1, 2, 3], [4, 5, 6]]) 
matrix2 = np.array([[7, 8], [9, -10], [11, 12]]) 
result_matrix = np.dot(matrix1, matrix2) 
print(result_matrix) 
#output
'''[[ 58  24] 
 [139  54]]'''