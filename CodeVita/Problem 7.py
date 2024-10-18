
# Problem  7: Polygon with Maximum Area
# You are given N number of coordinates and you have to create a polygon from these points such that they will make a polygon with maximum area.
# Note: coordinates provided in the input may or may not be in sequential form.
# Constraints
# 1 <= N <= 10
# Input:
# First line contains an integer N which depicts number of co-ordinates
# Next N lines consist of two space separated integer depicting coordinates of in form of xy
# Output:
# Print the maximum possible area possible by creating a polygon by joining the coordinates.
# If the area is in decimal form, print the absolute value as output.
# Time Limit (secs): 1
# Examples:

# Input:
# 4
# 0  0
# 2  0
# 0  2
# 2  2
# Output: 4
# Explanation:
# As we can imagine that these points will make a square shape and the maximum possible area made by the polygon will be 4.



# Solution
import math

class Solution:
    def maxArea(self, N, coordinates):
        if N <= 2:
            return None
        
        # Calculate the centroid of the points
        centroid_x = sum(x for x, y in coordinates) / N
        centroid_y = sum(y for x, y in coordinates) / N
        
        # Sort the points based on their angle with respect to the centroid
        def angle_from_centroid(point):
            x, y = point
            print(math.atan2(y - centroid_y, x - centroid_x))
            return math.atan2(y - centroid_y, x - centroid_x)
        
        coordinates.sort(key=angle_from_centroid)
        
        # Shoelace formula to calculate the area of the polygon
        area = 0
        for i in range(N):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[(i + 1) % N]  # Wrap around to the first vertex
            area += x1 * y2 - y1 * x2
        area = abs(area) / 2.0
        return area

if __name__ == '__main__':
    N = 4
    coordinates = [(0, 0), (3, 0), (0, 2), (3, 2)]
    s = Solution()
    print(s.maxArea(N, coordinates))  # Output: 4.0