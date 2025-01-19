# Copy here code of line function from previous exercise
def line(n, s):
    if s == "":
        print("*" * n)
    else:
        print(s[0] * n)

def square(size, character):
    # You should call function line here with proper parameters
    for i in range(size):
        line(size, character)
        i+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")