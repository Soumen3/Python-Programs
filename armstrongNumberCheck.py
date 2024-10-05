num=int(input('Enter a number:\t'))

def armstrong(num):
    temp=num
    length=0
    while temp!=0:
        length+=1
        temp//=10

    temp=num
    result=0
    while temp!=0:
        rem=temp%10
        result=result + rem**3
        temp//=10
        
    if num==result:
        return 1
    else:
        return 0

print('The number is armstrong') if armstrong(num) else print('The number is not armstrong')