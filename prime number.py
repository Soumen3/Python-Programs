num=int(input('Enter a number:'))
for i in range(2,(num//2)):
    if num%i==0:
        print('This is not a prime number')
        break
else:
    print('This is a prime number')
