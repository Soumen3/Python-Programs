from functools import reduce


l1=[1,2,3,4]
def square (a):
    return a**2

l2=list(map(square,l1))
print(l2)


l1=[1,2,3,4]
def square (a,b):
    return a**b 

s=reduce(square,l1)
print(s)




l1=[2,3,5,6,7,9,11,13,15]
def checkPrime(n):
    for i in range(2,n):
        print(i,n)
        if n%i==0:
            return False
    return True
filteredList=list(filter(checkPrime,l1))
print(filteredList)


