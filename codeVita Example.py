import math

# Function to calculate the distance between two points on the same face (arc distance)
def arc_distance(p1, p2):
    # Calculate the straight line distance between the two points
    straight_line_distance = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)
    # Arc distance (subtending 60 degrees at the center)
    arc_distance = (2 * math.pi * straight_line_distance) / 6
    return arc_distance

# Function to calculate the straight line distance between two points on different faces (surface distance)
def surface_distance(p1, p2):
    # Calculate the Manhattan distance (shortest distance along the surface of the cube)
    surface_dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])
    return surface_dist

# Function to check if two points are on the same face
def same_face(p1, p2):
    # Check if all but one of the coordinates match
    return (p1[0] == p2[0] and p1[1] == p2[1]) or \
           (p1[0] == p2[0] and p1[2] == p2[2]) or \
           (p1[1] == p2[1] and p1[2] == p2[2])

# Main function to calculate the total distance traveled by the beetle
def beetle_distance(N, points):
    total_distance = 0
    
    # Iterate over each consecutive pair of points
    for i in range(N - 1):
        p1 = points[i]
        p2 = points[i + 1]
        
        if same_face(p1, p2):
            # Calculate arc distance if on the same face
            distance = arc_distance(p1, p2)
        else:
            # Calculate surface distance if on different faces
            distance = surface_distance(p1, p2)
        
        # Round the distance to two decimal places
        distance = round(distance, 2)
        total_distance += distance
    
    return round(total_distance, 2)

# Input reading and parsing
N = int(input())
coords = list(map(float, input().split(',')))

# Group the coordinates into points (x, y, z)
points = [(coords[i], coords[i + 1], coords[i + 2]) for i in range(0, len(coords), 3)]

# Output the total distance traveled by the beetle
print(f"{beetle_distance(N, points):.2f}")
