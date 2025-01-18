# Write your solution here
def line(n, s):
    if s == "":
        print("*" * n)
    else:
        print(s[0] * n)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
    line(7, "%")
    line(10, "LOL")
    line(3, "")