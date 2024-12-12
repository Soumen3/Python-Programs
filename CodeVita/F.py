import math

def reflect_point(p, line):
    """Reflects point p across the line defined by two points (line[0], line[1]) and (line[2], line[3])."""
    x1, y1, x2, y2 = line
    px, py = p
    dx, dy = x2 - x1, y2 - y1
    norm = dx * dx + dy * dy
    a = (dx * dx - dy * dy) / norm
    b = 2 * dx * dy / norm
    rx = a * (px - x1) + b * (py - y1) + x1
    ry = b * (px - x1) - a * (py - y1) + y1
    return (round(rx, 2), round(ry, 2))

def folded_area(area, folding_line):
    side = math.sqrt(area)
    square_corners = [(0, 0), (0, side), (side, side), (side, 0)]
    x1, y1, x2, y2 = folding_line
    
    # Classify points into left and right of the folding line
    left_points = []
    right_points = []
    
    for x, y in square_corners:
        # Line equation: Ax + By + C = 0
        A, B, C = y2 - y1, x1 - x2, x2 * y1 - x1 * y2
        position = A * x + B * y + C
        if position < 0:
            left_points.append((x, y))
        else:
            right_points.append((x, y))
    
    # Reflect the left points across the folding line
    reflected_points = [reflect_point(p, (x1, y1, x2, y2)) for p in left_points]
    
    # Combine and deduplicate points
    all_points = set(right_points + reflected_points)
    
    # Sort by x, then by y
    sorted_points = sorted(all_points, key=lambda p: (p[0], p[1]))
    
    # Print the sorted points
    for x, y in sorted_points:
        print(f"{x:.2f} {y:.2f}")

# Example usage

area = int(input())
folding_line = tuple(map(int, input().split(" ")))

folded_area(area, folding_line)
