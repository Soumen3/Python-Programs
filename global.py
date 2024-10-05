# Python program to modify a global value inside a function
x = 15
def change():
	# using a global keyword to access a global variable
    global x
    # using global keyword to create a global variable
    global a
    a =50
	# increment value of a by 5
    x = x + 5
    print("Value of x inside a function :", x)


change()
print("Value of x outside a function :", x)
print('The value of global variable a is:',a)


