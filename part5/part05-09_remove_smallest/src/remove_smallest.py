# Write your solution here
import numpy as np
def remove_smallest(num: list):
    min_value = np.array(num).min()
    num = num.remove(min_value)
    return num

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)