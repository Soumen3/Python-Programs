        
def FarToCel(f):
    return ((f-32)/9)*5

def CelToFar(c):
    return (9*c)/5+32
    

choose=int(input('Enter 1 for farenheit to celcius:\nEnter 2 for celcius to farenheit:\n'))
match choose:
    case 1:
        f=float(input('Enter the temperature in farenheit: '))
        print(f"{f} deegre farenheit = {FarToCel(f)} degree celcius")
    case 2:
        c=float(input('Enter the tempaarture in farenheit: '))
        print(f"{c} deegre celcius = {CelToFar(c)} degree farenheit")
    case _:
        print('Enter valid choice')



