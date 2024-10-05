num1,num2,num3=float(input('Enter three numbers:')),float(input()),float(input())

if num1>=num2:
    if num1>=num3:
        print(f'The greatest number is {num1}')
    else:
        print(f'The greatest number is {num3}')
else:
    if num2>=num3:
        print(f'The greatest number is: {num2}')
    else:
        print(f'The greatest  number is {num3}')


print(f'The greatest number is {num1}') if num1>=num3 else print(f'The greatest number is {num3}')  if num1>=num2 else print(f'The greatest number is: {num2}') if num2>=num3 else print(f'The greatest  number is {num3}')