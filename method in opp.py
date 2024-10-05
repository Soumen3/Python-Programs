# type of method 


class student:

    school='ineuron'            # class variable

    def __init__(self):         
        self.marks=10

    def get_marks(self):        #  instance method   as it using the instance variable
        return self.marks

    @classmethod
    def get_school(self):       # class method   as it using the class vsriable
        return student.school

    @staticmethod               # by using this keyword you can call the this method by using object name       you don't need to pass self object
    def add(x,y):               # static  method   as it is not using any instance variable or any class variable
        return(x+y)


s1=student()
s2=student()

print(s1.marks)
print(student.get_school())
print(student.add(5,6))
print(s1.add(5,7))