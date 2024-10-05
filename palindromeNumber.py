num=int(input('Enter the number:'))
numToStr=str(num)
if num==int(numToStr[::-1]):
    print("The number is palindrome")
else: print("The number is not palindrome")


# basic way
def checkPalindrome(num):
    temp=num
    sto=0
    while temp!=0:
        rem=temp%10
        sto=sto*10+rem
        temp//=10
    if sto==num:
        return 1
    else:
        return 0
    
print('The number is palindrome ') if checkPalindrome(num) else print('THe number is not palindrome')