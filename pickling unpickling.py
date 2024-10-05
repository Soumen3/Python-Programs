import pickle

class student:

    def __init__(self,name,roll,address):
        self.name=name
        self.roll=roll
        self.address=address

    def display(self):
        print(f'name: {self.name} roll: {self.roll}, address: {self.address}')


f=open('student.pkl', 'wb')
std1=student('Soumen', 10, 'Keshpur')
std2=student('Akash', 11, 'Keshpur')

pickle.dump(std1,f)
pickle.dump(std2,f)
print('Pickling done!')
f.close()


# unpickling
f=open('student.pkl','rb')
data=pickle.load(f)
data2=pickle.load(f)
data.display()
data2.display()
print("Unpkling done!")
f.close()