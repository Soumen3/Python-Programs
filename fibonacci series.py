n=int(input('How many numbers you want to print:\t'))
f,s=0,1

for i in range(n):
    print(f,end=' ')
    f,s=s,f+s



'''Using recursion'''

print('\nUsing recursion:')

def fibo(a:int):
    if a==0:
        return 0
    if a== 1:
        return 1
    return (fibo(a-1))+(fibo(a-2))
for i in range(0,n):
    print(fibo(i),end=' ')
