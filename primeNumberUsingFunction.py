def is_prime(n):
    if n in[2,3]:
        return True
    if(n==1)or(n%2==0):
        return False
    r=3
    while r*r<=n:
        if n%r==0:
            return False
        r+=2
        return True
print(f"the number 25 is prime {is_prime(25)}, the number 23 is prime number {is_prime(23)}")
