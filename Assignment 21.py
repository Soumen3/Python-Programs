              #Assigment 21
                      #Rcurssion


# 1. Write a recursive python function to print first N natural numbers.

def printNnumbers(n):
    if n==0:
        return
    else:
        printNnumbers(n-1)
    print(n,end=' ')
    
n=int(input('Enter a number:\t'))
print(f'The {n} natural numbers are:')
printNnumbers(n)





# 2. Write a recursive python function to print first N natural numbers in reverse order

def printNnumbers(n):
    if n==0:
        return
    print(n,end=' ')
    printNnumbers(n-1)
    
n=int(input('Enter a number:\t'))
print(f'The {n} natural numbers in reverse order are:')
printNnumbers(n)




# 3. Write a recursive python function to print first N odd natural numbers


def print_N_odd_number(n):
    if n==0:
        return
    print_N_odd_number(n-1)
    print(n*2-1,end=' ')

n=int(input('Enter a number:\t'))
print(f'The {n} odd numbers are:')
print_N_odd_number(n)





# 4. Write a recursive python function to print first N odd natural numbers in reverse order

def print_N_odd_number(n):
    if n==0:
        return
    print(n*2-1,end=' ')
    print_N_odd_number(n-1)

n=int(input('Enter a number:\t'))
print(f'The {n} odd numbers in revevrse order are:')
print_N_odd_number(n)






# 5. Write a recursive python function to print first N even natural numbers.

def print_N_even_number(n):
    if n==0:
        return
    print_N_even_number(n-1)
    print(n*2,end=' ')

n=int(input('Enter a number:\t'))
print(f'The {n} even numbers are:')
print_N_even_number(n)






# 6. Write a recursive python function to print first N even natural numbers in reverse order.

def print_N_reverseEven_number(n):
    if n==0:
        return
    print(n*2,end=' ')
    print_N_reverseEven_number(n-1)

n=int(input('Enter a number:\t'))
print(f'The {n} even numbers in reverse order are:')
print_N_reverseEven_number(n)




# 7. Write a recursive python function to print squares of first N natural numbers

def print_square_N_numbers(n):
    if n==0:
        return
    else:
        print_square_N_numbers(n-1)
    print(n**2,end=' ')
    
n=int(input('Enter a number:\t'))
print(f'The squares of {n} natural numbers are:')
print_square_N_numbers(n)







# 8. Write a recursive python function to print cubes of first N natural numbers

def print_cubes_N_numbers(n):
    if n==0:
        return
    else:
        print_cubes_N_numbers(n-1)
    print(n**3,end=' ')
    
n=int(input('Enter a number:\t'))
print(f'The cubes of {n} natural numbers are:')
print_cubes_N_numbers(n)





# 9. Write a recursive python function to print first N multiples of a given number.

def n_multiplies(num,n):
    if n<1:
        return
    n_multiplies(num,n-1)
    print(num*n,end=' ')

num=int(input('Enter a number:\t'))
n=int(input('Enter the value of n:\t'))
print(f'The {n} multiplies of {num} are:')
n_multiplies(num,n)






# 10. Write a recursive python function to print a number in reverse order.

def reverse(num):
    if num<10:
        print(num,end="")
        return
    else:
        print(num%10,end='')
        reverse(num//10)
    
num=int(input('Enter a number:\t'))
print('The number in reverse is:')
reverse(num)
