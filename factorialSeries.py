def fact(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result


n=int(input("Enter the value of n: "))
even=0
odd=0
for i in range(1,n+1):
    if i%2==0:
        even=even+ i/fact(i)
    else:
        odd= odd + i/fact(i)

print(f"The rasult is {odd-even}")
