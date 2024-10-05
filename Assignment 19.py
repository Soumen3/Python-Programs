              # Assignment 19
              #               Functions

# 1. Write a python program to create a simple function which prints “MySirG” .

def print_name():
    print('MySirG')

print_name()







# 2. Write a python program to create a function which expects two arguments and print them in the function body.

def get(a,b):
    print('The values are:',a,b)

get(5,12)







# 3. Write a python program to create a function which expects an unknown number of arguments.

def unknown(*t):
    print('The value that are passed are:',t)
unknown(12,32,4,54,55,56,36,6,345,7435)







# 4. Write a python program to create a function which expects kwargs arguments

def kwargs(a,b):
    print('The division is:',a/b)
kwargs(b=3,a=12)







# 5. Write a python program to create a function which expects a list as an argument.

def take_list(list1):
    print('The list is :',list1)

lst=[12,32,'Soumen',443,45]
take_list(lst)







# # 6. Write a python program to create a function that finds a maximum of four numbers.

def maxNumber(lst):
    print('The maximum of the numbers is:',max(lst))

lst=[int(e) for e in input('enter four rnumbers seperated by space:\n').split()]
maxNumber(lst)







# 7. Write a python program to sum all the numbers in a list.
 
def sumofNumbers(lst):
    print('The sum if two numbers is:',sum(lst))

lst=[int(e) for e in input('enter numbers seperated by space:\n').split()]
sumofNumbers(lst)







# 8. Write a python program to multiply all the numbers in a list.

from math import prod

def product(lst):
    print('The multiply of the list is :',prod(lst))

lst=[int(e) for e in input('enter numbers seperated by space:\n').split()]
product(lst)






# 9. Write a python program to create a function to check whether a number falls in a given range.

def check(num, start, end):
    if num in range(start,end):
        print('The given number is present in the range')
    else:
        print('The given number is not present in the range')

start=int(input('Enter the starting range:\t'))
end=int(input('Enter the ending range:\t'))
num=int(input('Enter the nnumber you want to search:\t'))
check(num,start,end)





# 10. Write a python program to create a function to check whether a given number is even or odd.

def oddEven(num):
    print('The number is even' if num%2==0 else 'The number is odd')

num=int(input('Enter a number:\t'))
oddEven(num)