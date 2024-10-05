# 1. Write a python script to create a Profile class with 3 attributes (name, email, age).

class profile:
    name='soumen'
    email='soumensamanta112233@gmail.com'
    age=20

person1=profile()
print(person1.name)
print(person1.email)
print(person1.age)


        

# 2. Write a python script to update the above Profile class with encapsulation.

class profile:
    name='soumen'
    email='soumensamanta112233@gmail.com'
    age=20

    def update_details(self):
        profile.name=input('Enter person name:\t')
        profile.email=input('Enter email:\t')
        profile.age=int(input('Enter the age:\t'))


person1=profile()
print(person1.name)
print(person1.email)
print(person1.age)

person1.update_details()
print('\nThe details after update:')
print(person1.name)
print(person1.email)
print(person1.age)



# 3. Write a python script to update 2nd Question, change email and age to __email and __age.

class profile:
    name='soumen'
    __email='soumensamanta112233@gmail.com'
    __age=20

    def update_details(self):
        profile.name=input('Enter person name:\t')
        profile.__email=input('Enter email:\t')
        profile.__age=int(input('Enter the age:\t'))


person1=profile()
print(person1.name)

person1.update_details()
print('\nThe details after update:')
print(person1.name)





# 4. Write a python script to update 2nd Question, add a class variable (platform) and create a classmethod to access it.

class profile:
    name='soumen'
    email='soumensamanta112233@gmail.com'
    age=20
    platform='ineuron'

    def update_details(self):
        profile.name=input('Enter person name:\t')
        profile.email=input('Enter email:\t')
        profile.age=int(input('Enter the age:\t'))
    
    @classmethod
    def access_platform(self):
        return profile.platform


person1=profile()
print(person1.name)
print(person1.email)
print(person1.age)

person1.update_details()
print('\nThe details after update:')
print(person1.name)
print(person1.email)
print(person1.age)

print('The platform is:',person1.access_platform())




# 5. Write a python script to create a Calculator class with 2 methods for adding and subtracting 2 values.

class Calculator:

    def adding(self, num1,num2):
        return num1+num2


    def subtract(self, num1,num2):
        return num1-num2

obj1=Calculator()

print(obj1.adding(5,6))
print(obj1.subtract(5,6))





'''6. Write a python script to create a Calculator 2.0 class with 2 methods for multiplication and division of 2 values 
and inherit it from the Calculator class.'''

class Calculator_2:

    def multiplication(self,num1,num2):
        return num1*num2

    def division(self,num1,num2):
        return num1/num2

class Calculator(Calculator_2):

    def adding(self, num1,num2):
        return num1+num2

    def subtract(self, num1,num2):
        return num1-num2

obj1=Calculator()

print(obj1.adding(5,6))
print(obj1.subtract(5,6))
print(obj1.multiplication(5,6))
print(obj1.division(5,6))




# 7. Write a python script to create a Phone class with 2 methods to print the features (calling and sms).

class phone:

    def make_a_call(self):
        print('calling')
    
    def send_a_sms(self):
        print('sms')

user=phone()
user.make_a_call()
user.send_a_sms()
    



# 8. Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and Phone Class.

class phone:

    def make_a_call(self):
        print('calling')
    
    def send_a_sms(self):
        print('sms')

class Calculator_2:

    def multiplication(self,num1,num2):
        return num1*num2

    def division(self,num1,num2):
        return num1/num2


class Smartphone(phone,Calculator_2):
    pass

user=Smartphone()
user.make_a_call()
user.send_a_sms()
print(user.multiplication(5,6))
print(user.division(30,5))



'''9. Write a python script to create an application like Truecaller where names and numbers are stored. 
Truecaller class will have 2 methods (1st to fetch the name of a number and 2nd to add a new entry).'''

class truecaller:
    dct={
        9382532340:"Soumen",
        6295974532:"Akash",
        9586746525:'Prayas',
        9857451565:'Subhankar',
    }

    def add_a_new_entry(self,name, number):
        truecaller.dct[number]=name

    def fetch_data(self,number):
        print(number,':',self.dct[number])

user=truecaller()
user.add_a_new_entry("Priti",6325894255)
user.add_a_new_entry("najifa",9758642533)

user.fetch_data(9382532340)




'''10. Write a python script to add the new method in SmartPhone class which accepts Truecaller object 
as a parameter and call the fetch method of Truecaller.'''



class phone:

    def make_a_call(self):
        print('calling')
    
    def send_a_sms(self):
        print('sms')

class Calculator_2:

    def multiplication(self,num1,num2):
        return num1*num2

    def division(self,num1,num2):
        return num1/num2

class truecaller:
    dct={
        9382532340:"Soumen",
        6295974532:"Akash",
        9586746525:'Prayas',
        9857451565:'Subhankar',
    }

    def add_a_new_entry(self,name, number):
        truecaller.dct[number]=name

    def fetch_data(self,number):
        print(number,':',self.dct[number])


class Smartphone(phone,Calculator_2):
    def accept_truecaller(self,truecaller,number):
        truecaller.fetch_data(number)


Truecaller_user=truecaller()

smartphone_user=Smartphone()
smartphone_user.accept_truecaller(Truecaller_user,6295974532)