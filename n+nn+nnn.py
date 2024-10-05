num=int(input('Enter the number:'))
result=num+(num*10+num)+(num*100+(num*10+num))       # n+nn=nnn         like-   5+55+555
print('The result is',result)

# or

num=input('Enter the number:')
n1=int('%s'%num)
n2=int('%s%s'%(num,num))
n3=int('%s%s%s'%(num,num,num))
print('The result is',n1+n2+n3)