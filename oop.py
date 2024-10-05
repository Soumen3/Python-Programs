# object

# knows something- Attribute
# does something- method(function)




class computer:

    brand='hp'                  # class namespace

    def __init__(self):         # __init__() called autometically when object is created    self is representing the object which is created 
        self.cpu='ryzen5'       # instance namespace
        self.ram=8

    def show(self):
        print('Hello')
        print(self.cpu,self.ram)


com1=computer()         # creating object
com1.cpu='i7'           # you can update the value like this

com2=computer()         # you can pass the value of cpu and ram at the time of creating the object
# com2.cpu='i9'


print(com1.cpu)
print(com2.cpu)

com2.show()    # computer.show(com2)        -behind the scene com2.show() is like that
computer.show(com1)

print(computer.brand)
