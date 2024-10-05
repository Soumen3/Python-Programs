def maxArea(height):
        left = 0 
        right = len(height)-1

        water=0 

        while left < right :
            min_height = min (height[left], height[right])
            water_contains = min_height * (right-left)
            if water < water_contains :
                water = water_contains
            
            if height[left] < height[right]:
                left +=1
            else:
                right -= 1
        return water


print(maxArea([1,8,6,2,5,4,8,3,7])) # 49