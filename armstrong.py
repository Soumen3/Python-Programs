num=int(input('Enter a three digit number:\t'))
sum=0
temp=num
while temp>0:
    rem=temp%10
    sum+=rem**3
    temp//=10
print(f'{num} is an armstrong number' if sum==num else f'{num} is not an armstrong number')