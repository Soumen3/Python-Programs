row = int(input("Enter the number of row:\t"))

for i in range(row):
    for j in range(row):
        if i == 0 or i == row-1:
            print("*", end='')
            continue
        if j == 0 or j == row-1:
            print("*", end='')
        else:
            print(" ", end='')
    print()
