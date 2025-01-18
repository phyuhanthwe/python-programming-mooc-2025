# Write your solution here
import numpy as np
def list_sum(a, b):
    np_a = np.array(a)
    np_b = np.array(b)
    np_c = np_a + np_b
    c = np_c.tolist()
    return c

if __name__=="__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]