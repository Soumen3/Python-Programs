import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
def sine_curve():
    Fs= 8000
    f=5
    sample = 8000
    x=np.arange(sample)
    y=np.sin(2*np.pi*f*x/Fs)
    plt.plot(x, y)
    plt.xlabel('voltage(V)')
    plt.ylabel('sample(n)')
    plt.show()
def cosine_curve():
    Fs = 8000
    f= 5
    sample= 8000
    x = np.arange(sample)
    y = np.cos(2*np.pi*f*x/Fs)
    plt.plot(x, y)
    plt.xlabel('voltage(V)')
    plt.ylabel('sample(n)')
    plt.show()
def polynomial_curve():
    x= np.arange(-5, 5, 0.25)
    y= np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(x, y)
    F= 3+2*X + 4*X*Y + 5*X*X
    fig= plt.figure()
    ax= fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, F)
    plt.show()
def menu():
    print('1. Sine Curve')
    print('2. Cosine Curve')
    print('3. Polynomial Curve')
    print('4. Exponential Curve')
ch = 'y'
while(ch=='y'):
    menu()
    choice = int(input('Enter choice...'))
    if(choice ==1):
        sine_curve()
    elif(choice==2):
        cosine_curve()
    elif(choice==3):
        polynomial_curve()
    elif(choice==4):
        # exponential_curve(lambda x: 100*(np.power(0.8, x)), (0, 100))
        pass
    else:
        print('Wrong choice')
    ch = input('Do you want to continue (y/n)...')