s='bxbbxxb'

def palindrome(i,j):
    string=[]
    for e in range(i,j):
        string.append(s[e])
    
    string=''.join(string)
    string=str(string)
    

    # print(string)


    if string == string[::-1]:
        # print(string)
        return string
    

subStrings=[]
for i in range(len(s)):
    for j in range(i,len(s)):
        SubS=palindrome(i,j)
        subStrings.append(SubS)

# print(subStrings)


sLen=len(subStrings)
i=0
# for i in range(sLen):
while i<sLen:
    if subStrings[i] == None:
        del(subStrings[i])
        i-=1
        sLen-=1
    i+=1


maximumLenIndex=0
for i in subStrings:
    if len(i)> maximumLenIndex:
        maximumLenIndex=subStrings.index(i)


print(subStrings[maximumLenIndex])




