def grade(num):
    if num>=80:
        print(f"  {num}        A")
    elif num>=70:
        print(f"  {num}        B")
    elif num>=60:
        print(f"  {num}        C")
    elif num>=40:
        print(f"  {num}        D")
    else:
        print(f"  {num}        E")
        

a,b,c=float(input('Enter your three numbers:\n')),float(input()),float(input())

print('Number       Grade')
grade(a)
grade(b)
grade(c)
