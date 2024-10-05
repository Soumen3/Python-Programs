import numpy as np  
import matplotlib.pyplot as plt  
   
# Creating a sample dataset  
np.random.seed(23685736)  
N_samples = 100000  
no_bins = 25  
   
# Creating a random normal distribution using randn() method  
x_axis = np.random.randn(N_samples)  
y_axis = .6 ** x_axis + x_axis * np.random.randn(100000) + 90  
   
# Creating the histogram using the above data  
figure, axis = plt.subplots(figsize = (8, 3), tight_layout = True)  
   
axis.hist(x_axis, bins = no_bins)  
   
# Showing the plot  
plt.show()
