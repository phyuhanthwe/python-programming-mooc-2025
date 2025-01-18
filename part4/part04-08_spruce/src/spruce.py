# Write your solution here

def spruce(n):
    print("a spruce!")
    for i in range(1, n + 1):
        spaces = n - i
        stars = 2 * i - 1
        print(f"{' ' * spaces}{'*' * stars}{' ' * spaces}")
    print(f"{' ' * (n - 1)}{'*'}{' ' * (n - 1)}") 


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)