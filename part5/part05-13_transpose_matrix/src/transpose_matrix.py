# Write your solution here
def transpose(matrix: list):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            print(matrix)

if __name__=="__main__":
    l = [[1,2],[1,2]]
    (transpose(l))  