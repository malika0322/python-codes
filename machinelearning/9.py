#9. Create a histogram of a numerical column using NumPy and Matplotlib. 
import numpy as np 
import matplotlib.pyplot as plt 
data = np.random.randn(1000)  # Generating random data for demonstration 
hist, edges = np.histogram(data, bins=10) 
plt.hist(data, bins=edges, edgecolor='black', alpha=0.7) 
plt.title('Histogram of a Numerical Column') 
plt.xlabel('Values') 
plt.ylabel('Frequency') 
plt.show() 
#output
''''''