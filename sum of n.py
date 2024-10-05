n=int(input('Enter the value of n:\t'))

def sumN(n):
    if n<=1:
        return n
    return n+sumN(n-1)

print('The result is:\t',sumN(n))