# Write your solution here
def same_chars(text, a, b):
    scope = len(text) - 1
    if a > scope or b > scope or text[a] != text[b]:
        return False
    else:
        return True

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("coder", 1, 10))