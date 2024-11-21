# You are required to implement the following Function 
# def LargeSmallSum(arr)
# The function accepts an integers arr of size ’length’ as its arguments you are required to return the sum of second largest  element from the even positions and second smallest from the odd position of given ‘arr’
# Assumption:
# All array elements are unique
# Treat the 0th position as even
# NOTE
# Return 0 if array is empty
# Return 0, if array length is 3 or less than 3
# Example
# Input
# arr:3 2 1 7 5 4
# Output
# 7
# Explanation
# Second largest among even position elements(1 3 5) is 3
# Second smallest among odd position element is 4
# Thus output is 3+4 = 7
# Sample Input
# arr:1 8 0 2 3 5 6
# Sample Output
# 8


def LargeSmallSum(arr):
    if len(arr)<=3:
        return 0
    
    even_large, even_second_large = 0, 0
    odd_small, odd_second_small = float('inf'), float('inf')

    for i in range(len(arr)):
        if i%2 == 0:
            if arr[i] > even_large:
                even_second_large = even_large
                even_large = arr[i]
            elif arr[i] > even_second_large:
                even_second_large = arr[i]
        else:
            if arr[i] < odd_small:
                odd_second_small = odd_small
                odd_small = arr[i]  
            elif arr[i] < odd_second_small:
                odd_second_small = arr[i]

    return even_second_large + odd_second_small
            


arr = [1, 8, 0, 2, 3, 5, 6]
print(LargeSmallSum(arr))
