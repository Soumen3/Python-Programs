             # Assignment 20
             #                More on Functions

# 1. Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.

def unique(lst):
    temp_list=[]
    for e in lst:
        if e not in temp_list:
            temp_list.append(e) 
    return temp_list

lst=[int(e) for e in input('Enter element seperated by space:\n').split()]
print("The unique items are:\n",unique(lst))





# 2. Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.

def ckeck_prime(num):
    for i in range(2,(num//2)):
        if num%i==0:
            print('The number is not prime')
            break
    else:
        print('The numbers is prime')

num=int(input('Enter a number:\t'))
ckeck_prime(num)







# 3. Write a python program to create a function that prints the even numbers from a given list.

def even(lst):
    print('The even numbers are:')
    for i in lst:
        if i %2==0:
            print(i,end=' ')

lst=[1, 2, 3, 4, 5, 6, 7, 8, 9]
even(lst)





# 4. Write a python program to create a function that checks whether a passed string is palindrome or not.

def palindrom(string):
    if string==string[::-1]:
        print('The string is palindrom')
    else:
        print('The string is not palindrom')

string=input('Enter a string:\t')
palindrom(string)







# 5. Write a python program to create a function to find the Min of three numbers.

def minimum(*t):
    print('The minimum numbeer is the:',min(t))

a,b,c=eval(input('Enter three numbers:\n')),eval(input()),eval(input())
minimum(a,b,c)





# 6. Write a python program to create a function and print a list where the values are square of numbers between 1 and 30.

def square():
    lst=[(int(e))**2 for e in range(1,31)]
    print(lst)

square()





# 7. Write a python program to access a function inside a function.

def arithmetic():
    def add(a,b):
        print('The addition is ',a+b)
    return add
    
a,b=5,15
func=arithmetic()
func(a,b)





# 8. Write a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.


def check(string):
    u,l=0,0
    for i in string:
        if i.islower():
            l+=1
        elif i.isupper():
            u+=1
    print('Upper=',u,'   loewr=',l)

string=input('Enter a string:\t')
check(string)







# 9. Write a python program to create a function to check whether a string is a pangram  or not.

def pangram(string):
    alph="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(',')
    for i in alph:
        if i not in string:
            return i
    return -1
            

string=input('Enter a string:\n')
pan=pangram(string.lower())
if pan==-1:
    print('The string is pangram')
else:
    print(f'The string is not pangram. "{pan}" is not found')






# 10. Write a python program to create a function to check whether a string is an anagram or not.

string1=input('Enter first string:\t')
string2=input('Enter second string:\t')

def anagram(string1, string2):
    if len(string1)==len(string2):
        for i in string1:
            if i not in string2:
                return i
        else: return -1
    else: 
        print('The length of the string is not same....!')
        quit()

check=anagram(string1,string2)
if check==-1:
    print('The strings are anagram')
else:
    print(f'The strings are not anagram. "{check}" is not matching')
