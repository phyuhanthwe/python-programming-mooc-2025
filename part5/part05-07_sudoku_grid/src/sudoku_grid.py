def row_correct(sudoku, row_no):
    row = sudoku[row_no]
    non_zero = [num for num in row if num != 0]
    return len(non_zero) == len(set(non_zero))

def column_correct(sudoku, column_no):
    column = [sudoku[row_no][column_no] for row_no in range(9)]
    non_zero = [num for num in column if num != 0]
    return len(non_zero) == len(set(non_zero))

def block_correct(sudoku, row_no, column_no):
    block = []
    for i in range(3):
        for j in range(3):
            block.append(sudoku[row_no + i][column_no + j])
    non_zero = [num for num in block if num != 0]
    return len(non_zero) == len(set(non_zero))

def sudoku_grid_correct(sudoku):
    # Check all rows
    for row_no in range(9):
        if not row_correct(sudoku, row_no):
            return False

    # Check all columns
    for column_no in range(9):
        if not column_correct(sudoku, column_no):
            return False

    # Check all 3×3 blocks
    block_positions = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    for row_no, column_no in block_positions:
        if not block_correct(sudoku, row_no, column_no):
            return False

    return True

# Test cases
if __name__=="__main__":
    sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(sudoku_grid_correct(sudoku1))  # Output: False

    sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]
    print(sudoku_grid_correct(sudoku2))  # Output: True
    print(block_correct(sudoku2, 0, 2))
