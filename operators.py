a = 3
b = 5
# Arithmetic Operators
print('Arithmetic Operator')
print("the addition is", a+b)
print("the subtraction is", a-b)
print("the multiplication is", a*b)
print("the division is", a/b)
print("the Modules is", b % a)
print("the Exponential is", a**b)
print("the Floor division is", 27//b)  # it will return only decimal value

# Assignment operators
print('Assignment operators')
a = 12
a += 2
print("this is using += operator ", a)
a -= 2
print("this is using -= operator ", a)
a *= 2
print("this is using *= operator ", a)
a /= 2
print("this is using /= operator ", a)
a %= 2
print("this is using %= operator ", a)
a //= 2
print("this is using //= operator ", a)
a = 12
a &= 2
print("this is using &= operator ", a)
a = 12
a |= 2
print("this is using |= operator ", a)
a ^= 2
print("this is using ^= operator ", a)
a >>= 2
print("this is using >>= operator ", a)
a <<= 2
print("this is using <<= operator ", a)
a **= 2
print("this is using **= operator ", a)


# comperison operator
print('comperison operator')
b = (14 >= 7)  # returns a boolen value
print(b)
b = (14 <= 7)  # returns a boolen value
print(b)
b = (14 > 7)  # returns a boolen value
print(b)
b = (14 < 7)  # returns a boolen value
print(b)
b = (14 == 7)  # returns a boolen value
print(b)
b = (14 != 7)  # returns a boolen value
print(b)

# # Logical operator
print("logical operator")
x = 5
bool = (x < 5 and x > 7)
print(bool)
bool = (x < 5 or x > 7)
print(bool)
bool = not(x < 5 and x > 7)
print(bool)

# identity operator
print('identity operator')
x = 5
y = x
bool = (x is y)
print(bool)
bool = (x is not y)
print(bool)

# membrship operator
print('Membership operator')
x = [12, 20, 35]
bool = (12 in x)
print(bool)
bool = (12 not in x)
print(bool)

# bitwwise operator
print('bitwise AND of 12 and 14 is', 12 & 14)
print('bitwise OR of 12 and 14 is', 12 | 14)
print('bitwise XOR of 12 and 14 is', 12 ^ 14)
print('bitwise NOT of 14 is', ~14)

# a = 10 = 0000 1010 (Binary)
# a >> 1 = 0000 0101 = 5
# a >> 2 = 0000 0010 = 2
print('bitwise Zero Fill Right Shift of 10 is', 10 >> 1)
print('bitwise Zero Fill Right Shift of 10 is', 10 >> 2)


# a = 5 = 0000 0101 (Binary)
# a << 1 = 0000 1010 = 10
# a << 2 = 0001 0100 = 20 
print('bitwise Zero Fill Left Shift of 5 is', 5 << 1)
print('bitwise Zero Fill Left Shift of 5 is', 5 << 2)
