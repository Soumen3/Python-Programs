
''' 3. Write a menu driven program with the following options:
    a. Check whether a given set of three numbers are lengths of an isosceles
    triangle or not
    b. Check whether a given set of three numbers are lengths of sides of a right
    angled triangle or not
    c. Check whether a given set of three numbers are equilateral triangle or not
    d. Exit.'''

n1, n2, n3 = eval(input('enter three number:')), eval(input()), eval(input())
print('1. Check whether the given set of 3 numbers are length of an isoscele triangle or not')
print('2. Check whether the given set of 3 numbers are length of an right angle triangle or not')
print('3. Check whether the given set of 3 numbers are equilateral triangle or not')
print('4. EXIT')

ch = int(input('Enter your choice'))
match ch:
    case 1:
        if(n1 == n2 or n2 == n3 or n3 == n1):
            print('This is an isosceles triangle')
        else:
            print('This is not an isosceles triangle')
    case 2:
        if(n1**2 + n2**2 == n3**2 or n2**2 + n3**2 == n1**2 or n1**2 + n3**2 == n2**2):
            print('This is an right angle triangle')
        else:
            print('This is not an right angle triangle')
    case 3:
        if(n1 == n2 and n2 == n3):
            print('This is an equileteral triangle')
        else:
            print('This is not an equileteral triangle')
    case 4:
        quit()
    case _:
        print('Invalid choice....')







''' 4. Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen.'''

age=int(input('Enter your age:\t'))
match age:
        case age if age<10:
            print('You are kid')
        case age if age<20:
            print('You are Teen')
        case age if age<40:
            print('You are Young')
        case age if age<60:
            print('You are Experienced')
        case age if age>=60:
            print('You are Senior citizen')
            






'''5. Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number.'''

num=int(input('Enter a number:'))
match num%2==0:
    case 1:
        print('Saurabh Shukla')
    case 0:
        match num%2!=0 and num<0:
            case 1:
                print('Prateek Jain')
            case 0:
                print('Aditya Choudhary')







'''6. Write a python program to check whether a given string is a multiword string or single
word string using match case statement'''

s=input('Enter a string:\t').strip()

match s: 
    case s if " " in s:
        print('This is multiword word string')
    case s if " " not in s:
        print('This is a single word string')







'''7. Write a python program to check whether a given number is positive, negative or
zero using match case statement'''

n=int(input('Enter a number:\t'))
match n>0:
    case 1:
        print('The number is positive')
    case 0:
        match n<0:
            case 1:
                print('The number is negative')
            case 0:
                print('This is zero')







'''8. Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement'''

first=input('Enter first string:\t')
second=input('Enter second string:\t')
match first>second:
    case 1:
        print('Second strign comes before the first string')
    case 0:
        match second>first:
            case 1:
                print('The frst string comes before the second tring')
            case 0:
                print('The strings are identical')







'''9. Write a python script to check whether a given year is
    a. Non century leap year
    b. Century leap year
    c. Non century non leap year
    d. Century non leap year'''

y = int((input('Enter a year:\t')))
match y % 100 != 0 and y % 4 == 0:
    case 1:
        print('Non century leap year')
    case 0:
        match y % 100 == 0 and y % 400== 0:
            case 1:
                print('Centuary leap year')
            case 0:
                match y % 100 != 0 and y % 4 != 0:
                    case 1:
                        print('Non centuary non leap year')
                    case 0:
                        print('Centuary non leap year')








'''10. Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favourite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
      a. Yellow - Monday
      b. Blue - Tuesday
      c. Orange - Wednesday
      d. White - Thursday
      e. Black - Friday
      f. Red - Saturday   
      g. All other colours - Sunday'''

cl=input('enter your fevourite crolor:\t')
match 'yellow' in cl:
    case 1:
        print('monday')
    case 0:
        match 'blue' in cl:
            case 1:
                print('tuesday')
            case 0:
                match 'orange' in cl:
                    case 1:
                        print('wednesday')
                    case 0:
                        match 'whita' in cl:
                            case 1:
                                print('thursday')
                            case 0:
                                match 'black' in cl:
                                    case 1:
                                        print('friday')
                                    case 0:
                                        match 'red' in cl:
                                            case 1:
                                                print('saturday')
                                            case 0:
                                                print('sunday')
