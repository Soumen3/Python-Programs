# Implement the following Function 
# def differenceofSum(n. m)
# The function accepts two integers n, m as arguments Find the sum of all numbers in range from 1 to m(both inclusive) that are not divisible by n. Return difference between sum of integers not divisible by n with sum of numbers divisible by n.
# Assumption:
# n>0 and m>0
# Sum lies between integral range
# Example
# Input
# n:4
# m:20
# Output
# 90
# Explanation
# Sum of numbers divisible by 4 are 4 + 8 + 12 + 16 + 20 = 60
# Sum of numbers not divisible by 4 are 1 +2 + 3 + 5 + 6 + 7 + 9 + 10 + 11 + 13 + 14 + 15 + 17 + 18 + 19 = 150
# Difference 150 – 60 = 90
# Sample Input
# n:3
# m:10
# Sample Output
# 19

def differenceofSum(n, m):
    sum_divisible = 0
    sum_not_divisible = 0
    for i in range(1, m+1):
        if i % n == 0:
            sum_divisible += i
        else:
            sum_not_divisible += i
    return sum_not_divisible - sum_divisible

n=3
m=10

print(differenceofSum(n, m)) #19