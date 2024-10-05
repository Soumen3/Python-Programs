n=int(input('Enter the value of n:\t'))

def fact(i:int):
    re=1
    for e in range(1,i+1):
        re=re*e
    return re

result=0
for e in range(1,n+1):
    result=result+fact(e)

print('The result is',result)               
