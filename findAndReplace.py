import re
textLine = [strings for strings in input('Enter strings seperated by comma:\n').split(',')]

newList = []


for i in range(len(textLine)):
    newList.append(textLine[i].replace('love ', 'hate ').replace('Love ', 'Hate '))


print(newList)
