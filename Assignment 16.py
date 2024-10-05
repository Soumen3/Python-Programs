             # Assignment 16
                          # Tuple



# 1. Write a python script to store multiple items in a single variable ( Items are “Java”,“Python”, “SQL”, “C” ) using tuple

tup1=('Java', 'Python', 'SQL', 'C')
print(tup1)




# 2. Write a python program to store only one item using tuple.
tup1=('Python')
print(tup1)





# 3. Write a python program to reverse the tuple.

tup1=('Java', 'Python', 'SQL', 'C')
print('The reverse of the tuple is:',tup1[::-1])




# 4. Write a python program to Swap two tuples in Python.
tup1=('Java', 'Python', 'SQL', 'C')
tup2=('HTML', 'CSS', 'JS', 'DJANGO')
tup1,tup2=tup2,tup1

print('Tuple1 is:',tup1)
print('Tuple2 is:',tup2)




# 5. Write a python program to check if all items in the tuple are the same.

tup2=('HTML', 'CSS', 'JS', 'DJANGO')
for i in tup2:
    if tup2[0]!=i:
        print('All the items are not same')
        break
else:
    print('All the items are same')
    




# 6. Write a python program to divide the tuple into four variables. tuple1=(100, 200, 300, 400)

tuple1=(100, 200, 300, 400)
a,b,c,d=tuple1
print("a=",a)
print("b=",b)
print("c=",b)
print("d=",b)





# 7. Write a python program to copy elements 4 and 5 from the following tuple into a new tuple. tuple1=(1,2,3,4,5,6)

tuple1=(1,2,3,4,5,6)
new_tuple=()
new_tuple+=(tuple1[tuple1.index(4)],)
new_tuple+=(tuple1[tuple1.index(5)],)
print(new_tuple)





# 8. Write a python program to Sort a tuple of tuples by the second item. tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))

tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
tuple1 = list((('a', 21),('b', 37),('c', 11), ('d',29)))
length=len(tuple1)
for i in range(0,length):
    for j in range(i+1,length):
        if tuple1[i][1] > tuple1[j][1]:
            temp=tuple1[i]
            tuple1[i]=tuple1[j]
            tuple1[j]=temp

print(tuple(tuple1))





# 9. Write a python program to print the value 20 from given nested tuple tuple1 = ("Python", [10, 20, 30], (2, 4, 16))

tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
print(tuple1[1][1])





# 10. Write a python program to change the first item (22) of a list within the following tuple to 222.

tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=222
print(tuple1)