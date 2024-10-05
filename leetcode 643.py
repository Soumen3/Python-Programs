def findMaxAverage( nums, k):
    window_sum = sum(nums[0:k])
    result = window_sum
    right = k - 1

    for i in range(1, len(nums)-k+1):
        window_sum = window_sum + nums[right + 1] - nums[i-1]
        
        if window_sum > result:
            result = window_sum

        right += 1
        
    return result / k


print(findMaxAverage([0,4,0,3,2], 1)) # 12.75