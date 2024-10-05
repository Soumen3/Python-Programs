


class person:


    def __init__(self):
        self.__age=20           # by using '__' the variable is not accessable fron outside the class         private member


    def get_age(self):
        return self.__age


    def set_age(self, age):
        self.__age=age

    
p1=person()

p1.set_age(21)

print(p1.get_age())

print(p1.get_age())

# print(p1.__age)