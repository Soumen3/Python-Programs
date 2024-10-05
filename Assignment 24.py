# 1. Write a python program to create a user class with 3 properties : name, age, email.

class user:

    def __init__(self):
        self.name="Soumen"
        self.age=20
        self.email="soumensamanta112233@gmail.com"
    
    def get_data(self):
        print(self.name)
        print(self.age)
        print(self.email)

p1=user()

p1.get_data()




# 2. Write a python program to create a user class with a method to greet the user.

class user:

    def __init__(self):
        self.name="Soumen"
    
    def greet(self):
        print('Good Morning',self.name)

p1=user()
p1.greet()




# 3. Write a python program to create 2 objects of the user class and assign different values.

class user:

    def __init__(self, name, age):
        self.name=name
        self.age=age
        
    def get_data(self):
        print(self.name)
        print(self.age)

p1=user("Soumen",20)
p2=user("Akash",21)

p1.get_data()
p2.get_data()




# 4. Write a python program to init default values for user object using __init__ method.

class  user:

    def __init__(self):
        user.course='Full Stack Web Development Using Python'
    
p1=user()
p2=user()

print(p1.course)
print(p2.course)




# 5. Write a python program to delete the age property of the user.

class user():

    def __init__(self):
        self.age=20
        del self.age

p1=user()
print(p1.age)





# 6. Write a python program to create 3 user objects and find the youngest of all.

class user:

    def __init__(self,name, age):
        self.name=name
        self.age=age

    def age_compare(self, p2, p3):
        if self.age <= p2.age:
            if self.age <= p3.age:
                return self.age
            else:
                return p3.age
        else:
            if p2.age <= p3.age:
                return p2.age
            else:
                return p3.age 


p1=user('Soumen',20)
p2=user('Akash',22)
p3=user('Prayas',21)

print(p1.age_compare(p2,p3))






'''7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu, hdd)
 and 2 methods (showConfig() to print the values, __init__() to initialize the values).'''

class laptop:

    def __init__(self,brand,ram,cpu,hdd ):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd
        
    def showConfig(self):
        print('Brand is',self.brand)
        print('ram is ',self.ram,'GB')
        print('cpu is ',self.cpu)
        print('hdd is ',self.hdd)

lap1=laptop("hp",8,'Ryzen 5',None)
lap1.showConfig()




# 8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted order based on the ram size.

class laptop:

    def __init__(self,brand,ram,cpu,hdd ):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd
        
    def showConfig(self):
        print('Brand is',self.brand)
        print('ram is ',self.ram,'GB')
        print('cpu is ',self.cpu)
        print('hdd is ',self.hdd)

    def create_sorted_list(self, lap2,lap3):
        lst=[lap1,lap2,lap3]
        lst2=[]
        for i in lst:
            lst2.append(i.ram)

        lst2.sort()
        lst3=[]
        for e in lst2:
            for k in lst:
                if e==k.ram:
                    lst3.append(k)      
        return lst3

lap1=laptop("Dell",12,'i5',"1tb")
lap2=laptop("hp",8,'Ryzen 5',None)
lap3=laptop("Asus",16,'i5',None)

sorted_list=lap1.create_sorted_list(lap2,lap3)

for e in sorted_list:
    print('The rams in sorted order is :',e.ram)





# 9. Write a python program to create a School class and 3 instance variables and 1 class variable.

class school:
    school_name="Andichak High School(H.S)"

    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    
    def show_data(self):
        print('The name is:',self.name)
        print('The roll is:',self.roll)
        print('The marks is:',self.marks)
        print('The school name is:',school.school_name)

std1=school('Soumen',1,100)

std1.show_data()






'''10. Define a class Employee with instance object variables empid, name, salary. Write __init__() method in the class
 to initialize instance object variables. Also define instance methods to input fields and display field values'''


class employee:
    def __init__(self):
        self.input()
        self.empid
        self.name
        self.salary

    def input(self):
        self.empid=input("Enter id:\t")
        self.name=input('Enter name:\t')
        self.salary=int(input('Enter selary:\t'))

    def display(self):
        print('empid=',self.empid)
        print('Name=',self.name)
        print('Salary=',self.salary)

print('Fill emp1 details:')
emp1=employee()
print('\nFill emp2 details:')
emp2=employee()
print('\nFill emp3 details:')
emp3=employee()

print('\nemp1 details')
emp1.display()
print('\nemp2 details')
emp2.display()
print('\nemp3 details')
emp3.display()