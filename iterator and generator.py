from re import X


l1=[3,10,4,16,18,2]
it=iter(l1)
print(type(it))
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))




def f1():
    
    yield 10
    print("hello")
    yield 78
    yield 35
    yield 20

it1=f1()
print(it1)
print(type(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))




# create a generator to produce first n even natural number 
def evenGenerator(n):
    x=2
    while n:
        yield x
        x+=2
        n-=1
for e in evenGenerator(int(input('Enter a number:\t'))):
    print(e, end=" ")





# fibonacci series
print()
def fib(n):
    a,b=0,1
    while n:
        yield a
        a,b=b,a+b
        n-=1

for e in fib(10):
    print(e, end=' ')

