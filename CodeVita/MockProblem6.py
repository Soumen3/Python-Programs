def parse_input():
    grid = []
    for _ in range(9):
        row = input().strip().split()
        grid.append(row)
    allowed_numbers = input().strip().split()
    K = int(input().strip())
    return grid, allowed_numbers, K

def is_valid_sudoku(grid):
    def is_valid_block(block):
        block = [num for num in block if num != '0']
        return len(block) == len(set(block))
    
    for i in range(9):
        row = [grid[i][j] for j in range(9)]
        if not is_valid_block(row):
            return False
        
        col = [grid[j][i] for j in range(9)]
        if not is_valid_block(col):
            return False
        
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_valid_block(block):
                return False
    
    return True

def find_incorrect_cells(grid, allowed_numbers):
    incorrect_cells = []
    for i in range(9):
        for j in range(9):
            if grid[i][j].startswith('0') or grid[i][j].endswith('0'):
                if not is_valid_cell(grid, i, j, allowed_numbers):
                    incorrect_cells.append((i, j))
    return incorrect_cells

def is_valid_cell(grid, row, col, allowed_numbers):
    num = grid[row][col].strip('0')
    if num not in allowed_numbers:
        return False
    
    for i in range(9):
        if i != col and grid[row][i] == num:
            return False
        if i != row and grid[i][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if (i != row or j != col) and grid[i][j] == num:
                return False
    
    return True

def main():
    grid, allowed_numbers, K = parse_input()
    
    if is_valid_sudoku(grid):
        print("Won")
        return
    
    incorrect_cells = find_incorrect_cells(grid, allowed_numbers)
    
    if len(incorrect_cells) > K:
        print("Impossible")
    else:
        for cell in incorrect_cells:
            print(cell[0], cell[1])

if __name__ == "__main__":
    main()