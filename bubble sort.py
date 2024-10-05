
lst=[int(e) for e in input('Enter the element seperatedby space:').split(' ')]

for i in range(len(lst)):
    flag=0
    for j in range(len(lst)-i-1):
        if lst[j]>lst[j+1]:
            lst[j], lst[j+1]=lst[j+1],lst[j]
            flag=1
    if flag==0:
        break
print('After sorting the array:\n',lst)
