#         # Assignment - 11

# # 1. Write a python script to calculate sum of first N natural numbers

# N=int(input('Enter the value of N:\t'))
# sum=0
# while N:
#     sum=sum+N
#     N-=1
# print('The sum is:',sum)


# # 2. Write a python script to calculate sum of squares of first N natural numbers

# N=int(input('Enter the value of N:\t'))
# sum=0
# while N:
#     sum=sum+(N**2)
#     N-=1
# print('The sum is:',sum)


# # 3. Write a python script to calculate sum of cubes of first N natural numbers

# N=int(input('Enter the value of N:\t'))
# sum=0
# while N:
#     sum=sum+(N**3)
#     N-=1
# print('The sum is:',sum)



# # 4. Write a python script to calculate sum of first N odd natural numbers

# N=int(input('Enter the value of N:\t'))
# sum=0
# N=(2*N)-1
# while N>0:
#     sum=sum+N
#     N-=2
# print('The sum is:',sum)



# # 5. Write a python script to calculate sum of first N even natural numbers

# N=int(input('Enter the value of N:\t'))
# sum=0
# N=(2*N)
# while N>0:
#     sum=sum+N
#     N-=2
# print('The sum is:',sum)



# # 6. Write a python script to calculate factorial of a given number

# n=int(input("Enter the number:\t"))
# f=1
# for r in range(1,n+1):
#     f=f*r
# print("the factorial of given number is:",f)



# # 7. Write a python script to count digits in a given number

# num=int(input('Enter a number:\t'))
# len=0
# while num!=0:
#     len+=1
#     num=num//10
# print('The length of the number is:',len)



# # 8. Write a python script to calculate sum of digits of a given number

# num=int(input('Enter a number:\t'))
# l=0
# while num!=0:
#     l=l+(num%10)
#     num=num//10
# print('The sum of the digits is:',l)



# # 9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method).

# # decimal to binary convert
# n=int(input('Enter the number:\t'))
# re=""
# while n>0:
#     re=str(n%2)+re
#     n//=2
# print(re)



# # 10. Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)

# n=int(input('Enter the number:\t'))
# re=""
# while n>0:
#     re=str(n%8)+re
#     n//=8
# print(re)
