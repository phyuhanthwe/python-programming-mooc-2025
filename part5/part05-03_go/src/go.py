# Write your solution here
def who_won(lst: list):
    p1 = 0
    p2 = 0
    for row in lst:
        for i in row:
            if i == 1:
                p1 += 1
            elif i == 2:
                p2 += 1
    print(p1, p2)
    if p1 > p2:
        return 1
    elif p2 > p1:
        return 2
    else:
        return 0
    
if __name__=="__main__":
    game_board =  [[1, 2, 1], [0, 0, 1], [2, 1, 0]]
    print(who_won(game_board))