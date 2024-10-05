# creating tuple in python 
print('                 Creating tuple in python')
tup=('Soumen','Samanta','Hi','Boss')
print(tup)


# Accessing value in Tuples
print('\n                 Accessing value in Tuples')
print('value of tup[0]:',tup[0])
print('value of tup[2]:',tup[2])
print('value of tup[3]:',tup[3])

# Accessing value in Tuples using negative indexing
print('\n                 Accessing value in Tuples using negative indexing')
print('value of tup[-4]:',tup[-4])
print('value of tup[-2]:',tup[-2])
print('value of tup[-1]:',tup[-1])


# Concatination of tuple
print('\n                 Concatination of tuple') 
tuple1=(1,2,3,4)
tuple2=('Soumen','Samanta')
print(tuple1+tuple2)

# Nesting of tuples
print('\n                 Nesting of tuples')
tuple3=(tuple1,tuple2)
print(tuple3)


# Repetition of tuples
print('\n                 Repeatition of tuples')
tuple2=('Soumen',)*3
print(tuple2)
tuple2=('Soumen')*3
print(tuple2)


# Slicing tuple 
print('\n                 Slicing of tuple')
tuple1=(1,2,3,4)
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])


# Deleting a tuple 
print('\n                 Deleting a tuple')
del tuple3
print('Tuple deleted successfully......')


# Finding length of a tuple
print("\n                 Finding length of a tuple") 
print('the length of tuple1:',len(tuple1))

# Conveerting list to tuple
print('\n                 Convertiing list to tuple') 
list1=[0,1,2,3]
print(tuple(list1))
print(tuple('Python'))


# tuples in loop 
print('\n                Tuples in loop')
tup=('Sou')
n=5
for i in range(int(n)):
    tup=(tup,)
    print(tup)