                        # Assignment 12
                        #         More on loops

# 1. Write a python script to reverse a number.

n=int(input("Enter a number:\t"))
rev=0
while n:
      rem=n%10
      rev=rev*10+rem
      n//=10
print('The number in reverse is:',rev)

# or 

num= input('Enter a number:')
rev_num=num[::-1]
print('The number in reverse is:',int(rev_num))




# 2. Write a python script to check whether a given number is Prime or not

n=int(input("Enter a number:\t"))
for i in range(2,(n//2)+1):
        if n%i==0:
                print('The nmber is not prime')
                break
else:
        print('The number is prime')




# 3. Write a python script to print all Prime numbers under 100

for r in range(1,101):
        for i in range(2,(r//2)+1):
                if r%i==0:
                        break
        else:
                print(r,end=' ')




# 4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)

s=int(input("Enter starting range:\t"))
e=int(input('Enter ending range:\t'))
for i in range(s,e+1):
        for j in range(2,(i//2)+1):
                if i%j==0:
                        break
        else:
                print(i,end=' ')




# 5. Write a python script to find next prime number of a given number

n=int(input('Enter a number:\t'))
while 1:
        n+=1
        for i in range(2,(n//2)+1):
                if n%i==0:
                        break
        else:
                print('The next prime number is:',n)
                break



# 6. Write a python script to print first N prime numbers

n=int(input('Enter a number:\t'))
flag=1
while n:
        while 1:
                for i in range(2,(flag//2)+1):
                        if flag%i==0:
                                break
                else:
                        print(flag,end=' ')
                        n-=1
                        flag+=1
                        break
                flag+=1




# 7. Write a python script to check whether a given pair of numbers are co-Prime numbers or not.

n1,n2=int(input('enter a pair of numbers:')), int(input())
if n1>n2:s=n2
else:s=n1
for i in range(2,s+1):
        if n1%i==0 and n2%i==0:
                print('The numbers are not co-prime')
                break
else:
        print('The numbers are co-prime')




# 8. Write a python script to print first N terms of a Fibonacci series

n=int(input('How many numbers you want to print:\t'))
if n<=0:
        print('invalid input!.....')
        quit()
else:   
        f,s=0,1
        for i in range(n):
            print(f,end=' ')
            f,s=s,f+s
           


# 9. Write a python script to calculate LCM of two numbers
n1,n2=int(input('Enter two number:\n')),int(input())
if n1<n2:
        lcm=n1 
else: 
        lcm=n2
while True:
        if lcm%n1==0 and lcm%n2==0:
                print('The lcm is',lcm)
                break
        lcm+=1



# 10. Write a python script to calculate HCF of two numbers

n1,n2=int(input('Enter two numbers:')),int(input())
if n1>n2:
        s=n2
else:
        s=n1
for i in range(s,0,-1):
        if n1%i==0 and n2%i==0:
                print('The hcf is:',i)
                break




