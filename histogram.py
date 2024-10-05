import numpy as np  
from matplotlib import pyplot as plt  
  
# Creating a sample dataset  
array = np.array([23, 56, 87, 87, 98, 12, 76, 98, 34, 87, 67, 23, 87, 56, 34,  26, 85, 47, 35, 86, 76, 45, 86, 34, 37])
print(array)
   
# Creating a histogram using .hist() function  
figure, axis = plt.subplots(figsize = (8, 3))  
axis.hist(array, bins = [10,20,30,40,50,60,70,80,90,100])  
   
# Showing the plot   
plt.show()


'''
What is numpy?
numpy is a python library used for working with array. it is also function for working in domain linear algebra, fourier transform and matrix.
numpy was created in 2005 by travis oliphant. it is an open source project we should esily use it. python have the numerical method in the numpy 
library the numpy aims to provide an array object that is upto 50x faster than traditional python list. thi array object in numpy is 
called NDarray.


What is matplotlib?
matplotlib is a multi platforn data visualisation library built on numpy array and design to work with the border scipy stack it was introduce 
by jonhunter in the year 2002 
'''