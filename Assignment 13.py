               # Assignment-13
                              # list

# 1. Write a python script to store multiple items in a single variable ( Items are “Java” ,“Python”, “SQL”, “C” ) using list

l=['Java','python','SQL','C']
print(l)


# 2. Write a python script to get the data type of a list.

l=[12, "soumen", 12.54]
print(type(l))


# 3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])

mylist = ["Java", "C", "Python"]
print('The last item of the list is:',mylist[-1])



'''4. Write a python script to Change the values "SQL" and "Reactnative" with the values
"NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative",
"Javascript", "Python"]'''

thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
thislist[1]='NoSQL'
thislist[3]='Flutter'
print(thislist)


# 5. Write a python script to add an item to the end of the list (item “Python”. (mylist = ["Java", "SQL", "C", "Reactnative"]

mylist = ["Java", "SQL", "C", "Reactnative"]
mylist.append('Python')
print(mylist)


# 6. Write a python program to append elements from another list to the current list.(
# firstlist = ["Java", "Python", "SQL"]
# secondlist = ["C", "Cpp", "NoSQL"] )

firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]
# firstlist+=secondlist

for i in range(len(secondlist)):
    firstlist.append(secondlist[i])
print(firstlist)



# 7. Write a python program to Print all items by referring to their index number (thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

thislist =["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
l=len(thislist)
for i in range(l):
        print("index=",i,'-',thislist[i])



# 8. Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]

thislist = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"]
thislilst=thislist.sort()
print(thislist)


# 9. Write a Python script to create a list of city names taken from the user.

l=[e for e in input('Enter city names separated by space:\n').split()]
print(l)


# 10. Write a Python script to create a list, where each element of the list is a digit of a given number.

import random
l1=[e for e in input('Enter a list seperated by space:\t').split(" ")]
print(l1)
l=len(l1)
for i in range(l):
    l1[i]=int(random.choice(l1[i]))
print(l1)