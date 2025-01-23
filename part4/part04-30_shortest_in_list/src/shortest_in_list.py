# Write your solution here
import numpy as np

def shortest(l):
    min_len = len(min(l, key=len))
    return [s for s in l if len(s) == min_len][0]

if __name__=="__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    # shortest(my_list)
    result = shortest(my_list)
    print(result)