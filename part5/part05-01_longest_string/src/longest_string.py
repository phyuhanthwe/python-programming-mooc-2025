# Write your solution here
import numpy as np
def longest(lst: list):
    longest_str = ""
    for i in lst:
        if len(i) > len(longest_str):
            longest_str = i
    return longest_str

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))