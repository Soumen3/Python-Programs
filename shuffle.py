import random

lst = [1, 2, 3, 4, 5, 6, 7, 7]
random.shuffle(lst)
print(lst)

string = "Hey soumen"
str2="".join(random.sample(string, k=len(string)))
print(str2)



