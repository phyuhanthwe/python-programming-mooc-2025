# Write your solution here
def row_correct(sudoku, row_no):
    lst = sudoku[row_no]
    no_zero_lst = [value for value in lst if value != 0]
    if len(no_zero_lst) == len(set(no_zero_lst)):
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
    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))