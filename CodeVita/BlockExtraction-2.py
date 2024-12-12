def solve_block_extraction(N, M, matrix, target_color):
    # Create a deep copy of the matrix to avoid modifying the original
    grid = [row[:] for row in matrix]
    
    # Find all blocks in the matrix
    blocks = {}
    for r in range(N):
        for c in range(M):
            color = grid[r][c]
            if color not in blocks:
                blocks[color] = []
            blocks[color].append((r, c))
    
    # Track removed blocks
    removed_blocks = set()
    
    # Simulate gravity and block removal
    def apply_gravity():
        # Work from bottom to top
        for c in range(M):
            # Collect non-zero elements in this column from bottom
            column = [grid[r][c] for r in range(N-1, -1, -1) if grid[r][c] != 0]
            
            # Place non-zero elements back from bottom, fill rest with 0
            for r in range(N-1, -1, -1):
                if column:
                    grid[r][c] = column.pop(0)
                else:
                    grid[r][c] = 0
    
    # BFS to find blocks that need removal
    def find_blocks_to_remove(color):
        # Blocks that must be removed to access target
        removal_order = []
        
        # Find blocks that block the target block's extraction path
        blocking_colors = set()
        target_positions = blocks[color]
        
        # Check each possible row of target block
        for r, c in target_positions:
            # Check rows above this block
            for check_r in range(r):
                if grid[check_r][c] != 0 and grid[check_r][c] not in blocking_colors:
                    blocking_colors.add(grid[check_r][c])
        
        # Prioritize blocks from top rows first
        blocking_order = sorted(list(blocking_colors), key=lambda x: min(blocks[x], key=lambda pos: pos[0])[0])
        
        # Simulate removal and track blocks removed
        for block_color in blocking_order:
            # Skip if already removed
            if block_color in removed_blocks:
                continue
            
            # Mark block as removed
            for br, bc in blocks[block_color]:
                grid[br][bc] = 0
                removed_blocks.add(block_color)
            
            # Add to removal order
            removal_order.append(block_color)
            
            # Apply gravity after each block removal
            apply_gravity()
        
        return removal_order
    
    # Find and remove blocking blocks
    removals = find_blocks_to_remove(target_color)
    
    return len(removals)

# Read input
N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
target_color = int(input())

# Solve and print result
print(solve_block_extraction(N, M, matrix, target_color))