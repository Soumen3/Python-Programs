import pickle

car=['Thar','Fortuner','Audi','Marcedes','Rolls Royes']
bike=['H2R','BMW','Ducati','Hayabusa','Royel Enfield']


# picklilng
fileObject=open('car.pkl','wb')
pickle.dump(car,fileObject)
pickle.dump(bike,fileObject)
print('Pickling done\n')

# unpickling
fileObject=open('car.pkl','rb')
cars=pickle.load(fileObject)
print(cars)
bikes=pickle.load(fileObject)
print(bikes)
print('Unpickling done\n')
