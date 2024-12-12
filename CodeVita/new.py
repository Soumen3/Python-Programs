def min_presses_to_paint_wall(vertices, M):
    # Create a grid to represent the wall
    max_x = max(vertex[0] for vertex in vertices)
    max_y = max(vertex[1] for vertex in vertices)
    min_x = min(vertex[0] for vertex in vertices)
    min_y = min(vertex[1] for vertex in vertices)

    # Create a grid to mark painted areas
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    grid = [[0] * height for _ in range(width)]

    # Mark the wall area in the grid
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]
        if x1 == x2:  # Vertical line
            for y in range(min(y1, y2), max(y1, y2)):
                grid[x1 - min_x][y - min_y] = 1
        elif y1 == y2:  # Horizontal line
            for x in range(min(x1, x2), max(x1, x2)):
                grid[x - min_x][y1 - min_y] = 1

    # Count the number of presses needed
    presses = 0
    for x in range(width):
        for y in range(height):
            if grid[x][y] == 1:  # If this part of the wall needs painting
                presses += 1
                # Mark the area covered by the brush
                for dx in range(M):
                    for dy in range(M):
                        if x + dx < width and y + dy < height:
                            grid[x + dx][y + dy] = 0  # Mark as painted

    return presses

# Input reading
# N = int(input())
# vertices = [tuple(map(int, input().split())) for _ in range(N)]
# M = int(input())
N=4
vertices=[(0,0),(8,0),(8,1),(0,1)]
M=2

# Calculate and print the result
result = min_presses_to_paint_wall(vertices, M)
print(result)
