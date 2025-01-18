# Copy here code of line function from previous exercise
def line(n, s):
    if s == "":
        print("*" * n)
    else:
        print(s[0] * n)

def triangle(size):
    # You should call function line here with proper parameters
    for i in range(size):
        line(i+1, "#")
        i+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
