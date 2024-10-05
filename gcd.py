n1,n2=int(input("Enter two number:\n")),int(input())

i=1

while i<=n1 or i<=n2:
    if n1%i==0 and n2%i==0:
        gcd=i
    i+=1

print(f'The GCD of {n1} nd {n2} is {gcd}')