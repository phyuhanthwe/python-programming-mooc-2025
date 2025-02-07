# Write your solution here
def play_turn(lst, col, row, symbol):
    if 0 <= row <3 and 0 <= col < 3 and lst[row][col] == "":
        lst[row][col] = symbol
        return True
    else:
        return False

if __name__=="__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)