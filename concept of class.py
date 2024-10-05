class dog:
    eat='meat'
    def __init__(self,first,last):
        self.First=first
        self.Last=last

    def set(self):
        company='google'
        print(company)
        print(dog.eat)

dog1=dog('German shepherd','labrador')
dog1.set()
shadow=dog('dog','pet')
shadow.breed='germansheeper'
shadow.eat='bread'
print(shadow.eat)
print(shadow.__dict__)
print(dog.eat)
print(dog1.__dict__)
dog1.set()


# A Sample class with init method
class Person:

	# init method or constructor
	def __init__(self, name):
		self.Name = name
    
	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.Name)


p = Person('Nikhil')
p.say_hi()
print(p.__dict__)
