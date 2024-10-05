# 1/1+1/2+1/3.....1/n


n=int(input("enter the value of n: "))
re=0
for i in range(1,n+1):
    re=re+(1/i)

print("The result is: ",round(re,2))