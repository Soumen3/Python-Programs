print('The prime numbers between 6 to 96 are:\n')
def prime(i:int):
    for e in range(2,(i//2)+1):
        if i%e==0:
            return 
    print(i, end=' ')
for i in range(6,97):
    prime(i)