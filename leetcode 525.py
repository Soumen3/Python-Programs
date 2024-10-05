class Solution:
    def findMaxLength(self, nums):

        curr = 0
        maxx = 0
        prefix_sums = {}

        for i, elem in enumerate(nums):
            
            if elem == 0:
                curr -= 1
            else:
                curr+=1
            
            if curr == 0:
                maxx = max(i + 1, maxx)
            else:
                if curr in prefix_sums:
                    maxx = max(maxx, i - prefix_sums[curr])
                else:
                    prefix_sums[curr] = i
        
        return maxx


obj = Solution()
print(obj.findMaxLength([0,1,0,1,1, 0,1, 0,1,0,1,0,1,1,1,0,0,0])) # 2