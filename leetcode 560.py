from collections import Counter

class Solution:

    def subarraySum(self, nums, k) -> int:
        prefix_sums = {0: 1}
        current_sum = 0
        count = 0
        for num in nums:
        # Update the current prefix sum
            current_sum += num

            # Check if there is a prefix sum that when subtracted from current_sum equals k
            if (current_sum - k) in prefix_sums:
                count += prefix_sums[current_sum - k]

            # Update the dictionary with the current prefix sum
            if current_sum in prefix_sums:
                prefix_sums[current_sum] += 1
            else:
                prefix_sums[current_sum] = 1
        return count


obj = Solution()
print(obj.subarraySum([1,1,1,3,4,5,0,-10,15,-5,3,4,6,4,1,7,4,3,7,2,6], 5)) # 2