from collections import deque

def rotate(move, direction):
    x, y = move
    if direction == "forward":
        return x, y
    elif direction == "right":
        return y, -x
    elif direction == "left":
        return -y, x
    elif direction == "back":
        return -x, -y

def is_valid(grid, x, y, M, N):
    return 0 <= x < M and 0 <= y < N and grid[x][y] == 0

def min_moves(grid, source, destination, move_rule, M, N):
    # Directions corresponding to forward, right, left, and back
    directions = ["forward", "right", "left", "back"]
    
    # Initialize BFS queue
    queue = deque([(source[0], source[1], 0)])  # (row, col, moves)
    
    # Visited set to track visited cells
    visited = set()
    visited.add((source[0], source[1]))
    
    while queue:
        x, y, moves = queue.popleft()
        
        if (x, y) == (destination[0], destination[1]):
            return moves
        
        # Explore all 4 directions based on the move rule
        for direction in directions:
            new_move = rotate(move_rule, direction)
            new_x, new_y = x + new_move[0], y + new_move[1]
            
            if is_valid(grid, new_x, new_y, M, N) and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, moves + 1))
    
    # If no path is found, return -1 (unreachable)
    return -1


def main():
    M, N = map(int, input().split())
    
    grid = []

    for _ in range(M):
        grid.append(list(map(int, input().split())))
    
 
    src = tuple(map(int, input().split()))
    target = tuple(map(int, input().split()))
    
    move_rule = tuple(map(int, input().split()))
    
    result = min_moves(grid, src, target, move_rule, M, N)
    
    print(result)




main()
