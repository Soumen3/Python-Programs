from math import pi

def rectangle():
    a,b=float(input('Enter the lenght and width of rectangle:\n')),float(input())
    return a*b

def square():
    a=float(input("Enter the lenght of the arm of the square: "))
    return a*a

def circle():
    r=float(input('Enter the radius of the circle: '))
    return 2*pi*r

def triangle():
    a,b,c=float(input("Enter three sides of triangle:\n")),float(input()),float(input())
    if a+b<=c or a+c<=b or b+c<=a:
        print('The triangle is invalid!')
        return
    s=(a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5
    
print("Calculate The Area")
print("1 for rectangle")
print('2 for squre')
print('3 for circle')
print('4 for triangle')

choice=int(input('Enter your choice:'))
match choice:
    case 1:
        print(f'The area of the rectangle is {rectangle()}')
    case 2:
        print(f'The area of the square is {square()}')
    case 3:
        print(f'The area of the circle is {circle()}')
    case 4:
        print(f'The area of the triangle is {triangle()}')
    case _:
        print('Invalid choice!')
