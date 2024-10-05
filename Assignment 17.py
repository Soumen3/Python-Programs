              # Assignment 17
                             # set


# 1. Write a python program to store all the programming languages known to you using Set.

language={'C',"C++",'Java','Python','HTML','css','javaScript'}
print(language)




# 2. Write a python program to store your own information {name, age, gender, so on..}

details={'Soumen', 20, 'Male', 'Student'}
print(details)




# 3. Write a python script to get the data type of a Set.

details={'Soumen', 20, 'Male', 'Student'}
print('Type is:',type(details))




# 4. Write a Python script to find if “Python” is present in the set thisset = {"Java", "Python", "Django"}

thisset = {"Java", "Python", "Django"}

if 'Python' in thisset:
    print('Python is present in the set')
else:
    print('Python is not present in the set')





# 5. Write a python program to add items from another set to the current set. 
# thisset = {"Java", "Python", "SQL"} 
# secondset= {"C", "Cpp", "NoSQL"}

thisset = {"Java", "Python", "SQL"} 
secondset= {"C", "Cpp", "NoSQL"}

thisset.update(secondset)
print(thisset)






# 6. Write a python program to add elements of list to a set
# thisset = {"Python", "Django", "JavaScript"}
# mylist = ["Java", "C"]

thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]

thisset.update(set(mylist))
print(thisset)




# 7. Write a python program to remove last item of the given set
# thisset = {"Python", "Django", "JavaScript", “SQL”}

thisset = {"Python", "Django", "JavaScript", 'SQL'}
thisset.remove('SQL')
print(thisset)





# 8. Write a python program to delete the set completely.

thisset = {"Python", "Django", "JavaScript", 'SQL'}
thisset.clear()
print(thisset)





# 9. Write a python program to loop through the set and print values
# thisset = {"Python", "Django", "JavaScript", “SQL”}

thisset = {"Python", "Django", "JavaScript", "SQL"}
for i in thisset:
    print(i)





# 10. Write a python program to find the maximum and minimum value in a set.

value={21,34,54,3,5,65,4,34,546,75,43}
print('The maximum number is:',max(value))