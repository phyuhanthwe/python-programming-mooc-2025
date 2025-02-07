# Write your solution here
import copy
def transform(sudoku):
    lst = []
    for row in sudoku:
        sub_lst = []
        for i in row:
            if i != 0:
                sub_lst.append(i)
            else:
                sub_lst.append("_")
        lst.append(sub_lst)
    return lst

def print_sudoku(sudoku: list):
    lst = transform(sudoku)
    for i, row in enumerate(lst):
        for j, item in enumerate(row):
            print(item, end=" ")
            if j in [2, 5]:
                print("", end=" ")
        print("")
        if i in [2, 5]:
            print("")


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    grid_copy = copy.deepcopy(sudoku)  
    grid_copy[row_no][column_no] = number  
    return grid_copy  

if __name__=="__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 1, 1, 5)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)