
from time import sleep
from threading import *

# Hello class
# Hi class
# Main class

class Hello():
    def run(self):
        for i in range(5):    
            print("Hello")
            sleep(2)



class Hi():
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(2)


obj1=Thread(target=Hello.run(Hello))
obj2=Thread(target=Hi.run(Hi))
print("Welcome to the session")
print("We are learning threads")
x = 9

obj1.start()
obj2.start()

obj1.join()
obj2.join()

print("Bye")
