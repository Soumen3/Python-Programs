age = int(input('Enter your age:\t'))
if age > 18:
    print('You are sinior citizen now')
else:
    print('You are not sinior citizen now')


if age>10:
    if age>20:
        print('Your age is more than 20')
    else:
        print("your age is more than 10")
else:
    print("your age is less than 10")


if(age<5):
    print('your age is less than 5')
elif age<15:
    print('your age is less than 15')
elif age<20:
    print('your age is less than 20')
else:
    print("your age is more than 20")


# short hand if-else
print('you are eligible to drive car') if age >18 else print('you are not eligible to drive car')