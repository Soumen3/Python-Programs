import math as m
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-4*m.pi, 4*m.pi, 0.2)
f=2*np.exp(-2*(x-1.0)**2)
g=4*np.exp(-5*(x-1.0)**2)
plt.plot(x,f,"r")
plt.plot(x,g,"y")
plt.xlabel("x")
plt.ylabel("Function")
plt.legend(["x vs f", "x vs g"])
plt.show()