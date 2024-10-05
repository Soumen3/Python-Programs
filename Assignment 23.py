#                   # Assignment 23
#                   #               Iterator, Generator and Decorator


# # 1. Use iter and next method to access all the elements of a given set using while loop

# set1={1,2,3,4,5,6,7,8,9,10}
# it = iter(set1)
# length=len(set1)
# while length!=0:
#     print(next(it),end=' ')
#     length-=1




# # 2. Create a generator to produce first n odd natural numbers

# def odd(i):
#     x=1
#     while i:
#         yield x
#         x+=2
#         i-=1
# n=int(input('enter the value of n:\t'))
# for i in odd(n):
#     print(i,end=' ')





# # 3. Create a generator to produce first n even natural numbers

# def even(i):
#     x=2
#     while i:
#         yield x
#         x+=2
#         i-=1
# n=int(input('enter the value of n:\t'))
# for i in even(n):
#     print(i,end=' ')







# # 4. Create a generator to produce squares of first N natural numbers

# def square(i):
#     n2=i
#     a=1
#     while n2:
#         yield a**2
#         a+=1
#         n2-=1
# n=int(input('enter the value of n:\t'))
# for i in square(n):
#     print(i,end=' ')





# # 5. Create a generator to produce first n terms of Fibonacci series

# def fibo(i):
#     f,s=0,1
#     for e in range(i):
#         if e<=1:
#             yield e
#         else:
#             yield f+s 
#             f,s=s,f+s
    
# num=int(input('enter the number:\t'))
# print('The fibonacci series is:')

# for i in fibo(num):
#     print(i ,end=' ')







# # 6. Create a generator to produce first n prime numbers

# def prime(i):
    
#     n=1
#     while i:
#         flag=0
#         for k in range(2,n//2+1):
#             if n%k==0:
#                 flag=1
#         if flag==0:
#             yield n
#             i-=1
#         n+=1       

# num=int(input('Enter a number :\t'))
# print(f'first {num} prime numbers are:')

# for e in prime(num):
#     print(e,end=' ')
