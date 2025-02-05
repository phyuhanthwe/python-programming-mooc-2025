# Write your solution here
def block_correct(sudoku, r, c):
    block = []  
    for i in range(3):
        for j in range(3):
            block.append(sudoku[r + i][c + j])
    non_zero = [v for v in block if v != 0]
    if len(non_zero) == len(set(non_zero)):
        return True
    else:
        return False

if __name__=="__main__":
    sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]]
    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))