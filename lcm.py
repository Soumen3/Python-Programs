# n1,n2=int(input("Enter two number:\n")),int(input())
n1=10
n2=15
# i=1

# while i<=n1 or i<=n2:
#     if n1%i==0 and n2%i==0:
#         gcd=i
#     i+=1


# lcm=n1*n2/gcd

# print(f'The LCM of {n1} nd {n2} is {lcm}')



# process 2
if n1<n2:
    great=n2
else:
    great=n1

while (True):
    if great%n1==0 and great%n2==0:
        lcm=great
        break
    great+=1
print('the lcm is ',lcm)
