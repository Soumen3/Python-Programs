# ch=input('Enter a character:\t')
# print(f'The ascii value of {ch} is:',ord(ch))





char=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in char:
    print(ord(i.upper()),end=' ')

print()
for i in char:
    print(ord(i),end=' ')