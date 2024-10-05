'''pascal's triangle'''

def fact(n: int):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

def ncr( n:int, r:int):
    result=fact(n)/(fact(n-r)*fact(r))
    return result

row=int(input('How may row do you want to enter:\t'))
print("The pascal's triangle is:")
space=row
for i in range(row):
    for j in range(0,space):
        print('  ',end='')
    for k in range(0,i+1):
        print(int(ncr(i,k)),end="   ")
    print()
    space-=1




