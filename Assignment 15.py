#                  Assignment 15
#                              string


# 1. Write a python script to create a String in 3 different possible ways

str1='creating a string using single quotes'
str2="creating a string using double quotes"
str3='''ctreating 
string
using 
triple quote'''
print(str1)
print(str2)
print(str3)




# 2. Write a python script to Get the characters from the start to position 5 (Given String “iNeuron” using the slice syntax)

str1='iNeuron'
print('From the start to position 5:',str1[0:5])




# 3. Write a python script to Get the characters from position 2 to position 5 (Given String “Hello Learners” using the slice syntax)

str1='Hello Learners'
print('From position 2 to position 5:',str1[1:5])





# 4. Write a python script to demonstrate String Concatenation adding space in between ( Given Strings a=”Learning” b=”Python” )

a,b='Learning','Python'
print(a+' '+b)
print(a,b)




# 5. Write a python script to get the count of total number of characters in String a= “iNeuron”

a='iNeuron'
print('Total number of character is:',len(a))




# 6. Write a python script to reverse a String. (“iNeuron”)
a='iNeuron'
print('the reverse of the string is:',a[::-1])




# 7. Write a python script to determine whether a string contains a specific substring.

name='Soumen Samanta'
search=input('Enter a substrig:\t')

if search in name:
    print('The substring is present in the string')
else:
    print('The substring is not present in the string')





# 8. Write a python script to check if a string contains only numbers.
str1=input('Enter a string:\t')
if str1.isnumeric():
    print('The string contains only numbers.')
else:
    print('The string contains not only numbers.')
    




# 9. Write a python script to check if a string contains only characters of the alphabet.

str1=input('Enter a string:\t')
if str1.isalpha():
    print('The string contains only alphabet.')
else:
    print('The string contains not only alphabet.')





# 10. Write a python script to convert an integer to a string.

num=int(input('Enter a number:\t'))
print('The string format of the number is',str(num))