                        #program 1

a=7
b=0
c=0
try:
    c=a/b
except Exception as e:
    print('You can not devide by 0:',e)
print(c)
print('Bye')




      #                  program 2


a=7
b=int(input('enter a value:'))
c=0
try:
    c=a/b
except ZeroDivisionError as e:
    print('You can not devide by 0:', e)
print(c)
print('Bye')




                        #program 3


a=7

try:
    print('File open')
    b=int(input('enter a value:'))
    c=a/b
    print('The result is',c)
    
except ValueError:
    print('You have enter invalid value')

except ZeroDivisionError:
    print('Division by 0 is not possible')

except Exception:
    print('Some exception has occured')
finally:
    print('File closed')
print('Bye')








                        #program 4


a=7

try:
    print('File open')
    b=int(input('enter a value:'))
    if a==b:
        raise ArithmeticError
    c=a/b
    print('The result is',c)
    
except ValueError:
    print('You have enter invalid value')

except ZeroDivisionError:
    print('Division by 0 is not possible')

except ArithmeticError:
    print('The number cannot be same')

except Exception:
    print('Some exception has occured')
finally:
    print('File closed')
print('Bye')