# Copy here code of line function from previous exercise and use it in your solution
def line(n, s):
    if s == "":
        print("*" * n)
    else:
        print(s[0] * n)

def shape(n, cha1, m, cha2):
    for i in range(n):
        line(i+1, cha1)
        i+=1
    for i in range(m):
        line(n, cha2)
        i+=1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")