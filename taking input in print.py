# print('Enter two numbers:')
# x,y=float(input()), float(input())
# print('The addition result is:',x+y)





# print('Enter a number:')
# num=float(input())
# print('The square root of the numbeer is:',num**0.5)





# ch=input('Enter a character:')
# if (ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
#     print('This is an alphabet')
# else:
#     print('This not an alphabet')





# lst=['a','e','i','o','u','A','E','I','O','U']
# ch=input('Enter a character:')
# if ch in lst:
#     print('The alphabet is vowel')
# else:
#     print('The alphabet is a consonant')




# num=float(input('Enter an number:\t'))
# print('The number is positive') if num>0 else print('The number is non positive')




# num=float(input('Enter an number:\t'))
# print('it is divisible  by 5') if num%5==0 else print('it is not divisible by 5')




# num=float(input('Enter a number:\t'))
# print('it is odd' if num%2!=0 else 'it is even')




# print('Enter two word:')
# x,y=str(input()),str(input())
# print(x,'\n'+y) if x<y else print(y,'\n'+x)





# n1, n2, n3=float(input('Enter the number:\n')),float(input()),float(input())
# if n1>n2:
#     if n1>n3:
#         print('The greatest number is',n1)
#     else:print('The greatest number is',n3)
# elif n2>n3:print('The greatest number is',n2)
# else:print('The greatest number is',n3)

# # or
# print('The greatest number is',end=' ')
# print(n1 if n1>n3 else n3 if n1>n2 else n2 if n2>n3 else n3)



# # enter a month number and display the number of  days in the month
# m=int(input('Enter month number:\n'))
# if m>0 and m<=7 and m%2!=0:
#     print('The number of days in month is: 31')
# elif m>7 and m<=12 and m%2==0:
#     print('The number of days in month is: 31')
# else:
#     print('The number of days ii the month is: 30')

# # or
# if m in(1,3,5,7,8,10,12):
#     print('31 days')
# elif m in (4,6,9,11):
#     print('30 ddays')
# else:
#     print('28 or 29 days')






# cn=complex(input('Enter the complex number:\n'))
# print('the real part is',cn.real)
# print('the imaginary part is',cn.imag)





# file=open('soumen.txt','r')
# for i in file:
# print(file.read())
# print(i,end="")

# print(file.read(7))





# file=open('soumen.txt','w')
# file.write('This is a write command')
# file.write('\nit use to write')
# file.close()






# file=open('soumen.txt','w')
# file.write('\nThis is a write command')
# file.rstrip()
# file.close()
# with open('soumen.txt', "w+") as sou:
#     sou.write('\nHello every one')
#     data=sou.read()

# print(data)







# import random
# lst=['Green', 'Violet', 'Red']
# print(random.choice(lst))






# with open('soumen.txt','r') as sou:
#     data= sou.readlines()
#     for line in data:
#         word=line.split()
#         print(word)
# # print(data)
# num=eval(input('Enter a number:\n'))
# print(num,type(num))






# print('Enter three even number:')
# i=1
# while i<=3:
#     n=eval(input())
#     if n%2!=0:
#         print('You lose the game')
#         break
#     i+=1
# if i==4:
#     print('You are the winner')







# m=int(input('Enter an minth number:\n'))

# match m:
#     case 1:print('The number of daays is 31')
#     case 2:print('The number of daays is 28')
#     case 3:print('The number of daays is 31')
#     case 4:print('The number of daays is 30')
#     case 5:print('The number of daays is 31')
#     case 6:print('The number of daays is 30')
#     case 7:print('The number of daays is 31')
#     case 8:print('The number of daays is 31')
#     case 9:print('The number of daays is 30')
#     case 10:print('The number of daays is 31')
#     case 11:print('The number of daays is 30')
#     case 12:print('The number of daays is 31')






# n1,n2=int(input('Enter two numbers:\t')), int(input())
# op=input('enter the operation:\t')

# match op:
#     case "+":
#         print(n1+n2)
#     case '-':
#         print(n1-n2)
#     case '*':
#         print(n1*n2)
#     case '/':
#         print(n1/n2)








#''' # convert km to mile'''
# km=eval(input('Enter a distance in km:\t'))
# print('The distance in mile is',km*0.621)






# '''area of a triangle'''
# a,b,c=eval(input('Enter the length if three arms of the triangle:\n')),eval(input()),eval(input())
# s=(a+b+c)/2
# print('The area of the triangle is:',(s*(s-a)*(s-b)*(s-c))**0.5)






# '''swap two number'''
# a,b=eval(input('Enter two numbers:\n')),int(input())
# a=a+b
# b=a-b
# a=a-b
# print(f'The value of a is {a} and value of b is {b}')






# '''evaluate the of quadritic equation'''
# a,b,c=float(input('Enter the values of a, b and c:\n')),float(input()),float(input())
# x1=(-b+(((b**2)-4*a*c)**0.5))/2*a
# x2=(-b-(((b**2)-4*a*c)**0.5))/2*a
# print(f'The value of x1 is {x1} and value of  x2 is {x2}')








# n=int(input('Enter the value of n:\t'))
# x=int(input('Enter the value of x:\t'))
# s=0
# for a in range(1,n+1):
#     s=s+(x*a)
# print(s)




# s1,s2=input(),input()
# print((s2,s1) if s1>s2 else(s1,s2))








# N=int(input('Enter the value of n:\t'))
# for i in range(1,11):
#     print(N*i,end=' ')



# # multiplication table
# num=eval(input('Enter a number:\t'))
# print('The table is:')
# for i in range(1,11):
#     print(f'{num} * {i} = {num*i}')