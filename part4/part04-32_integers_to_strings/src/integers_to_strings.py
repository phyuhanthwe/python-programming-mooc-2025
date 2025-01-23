# Write your solution here
import numpy as np
def formatted(l):
    s = []
    for i in l:
        s.append(f"{i:.2f}")
    return s

if __name__=="__main__":
    my_list = [1.00023, 0.987, 0.55543, 1.76]
    # my_list = [1.234]
    new_list = formatted(my_list)
    print(new_list)
