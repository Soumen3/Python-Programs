          # Assignment 22
          #           More on recursion


# 1. Write a recursive python function to calculate sum of first N natural numbers

def sum(num):
    if num==0:
        return 0
    return num+(sum(num-1))

num=int(input('Enter a number:\t'))
print(f'The addition of {num} natural numbers is: {sum(num)}')





# 2. Write a recursive python function to calculate sum of first N odd natural numbers

def sum(num):
    if num<=1:
        return 1
    return num+(sum(num-2))

num=int(input('Enter the value of N:\t'))
print(f'The addition of {num} odd natural numbers is: {sum(num*2-1)}')







# 3. Write a recursive python function to calculate sum of first N even natural numbers

def sum(num):
    if num<=2:
        return 2
    return num+(sum(num-2))

num=int(input('Enter the value of N:\t'))
print(f'The addition of {num} even natural numbers is: {sum(num*2)}')




# 4. Write a recursive python function to calculate sum of squares of first N natural numbers

def sum_of_square(num):
    if num<=0:
        return 0
    return (num**2)+(sum_of_square(num-1))

num=int(input('Enter the value of N:\t'))
print(f'The squares of {num}  natural numbers is: {sum_of_square(num)}')




# 5. Write a recursive python function to calculate sum of cubes of first N natural numbers

def sum_of_square(num):
    if num<=0:
        return 0
    return (num**3)+(sum_of_square(num-1))

num=int(input('Enter the value of N:\t'))
print(f'The cubes of {num}  natural numbers is: {sum_of_square(num)}')





# 6. Write a recursive python function to calculate the factorial of a number.

def fact(num):
    if num==1:
        return 1
    return num*fact(num-1)

num=int(input('Enter the number:\t'))
print('The factorial of the given number is:',fact(num))






# 7. Write a recursive python function to calculate sum of the digits of a given number

def sum_of_digits(num):
    if num%10==0:
        return num
    return (num%10)+(sum_of_digits(num//10))

num=int(input('Enter a number:\t'))
print('The addition of the digits is:\t',sum_of_digits(num))







# 8. Write a recursive python function to print binary of a given decimal number.

def binary(num):
    if num<2:
        print(num,end='')
        return
    binary(num//2)
    print(num%2,end='')
    return

num=int(input('Enter a decimal number:\t'))
print('The binary number of the given number is:',end=' ')
binary(num)






# 9. Write a recursive python function to print octal of a given decimal number

def octal(num):
    if num<8:
        print(num,end='')
        return
    octal(num//8)
    print(num%8,end='')
    return

num=int(input('Enter a decimal number:\t'))
print('The octal number of the given number is:',end=' ')
octal(num)






# 10. Write a recursive python function to find the Nth term of the Fibonacci series.

def nth_fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return nth_fibonacci(n-1) + nth_fibonacci(n-2)

n=int(input('ENter the value of n:\t'))
print('The nth term of fibonacci serise is:',nth_fibonacci(n-1))