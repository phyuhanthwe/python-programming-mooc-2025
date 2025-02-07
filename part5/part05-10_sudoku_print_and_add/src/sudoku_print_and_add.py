# Write your solution here
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


def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number


if __name__=="__main__":
    sudoku  = [
    [1, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)