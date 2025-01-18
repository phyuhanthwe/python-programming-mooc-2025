# Write your solution here
def distinct_numbers(l):
    s = set(l)
    distinct_l = list(s)
    return sorted(distinct_l)
if __name__=="__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    my_list1 = [-1, -2, -1, -2, -3, -3, -3, 0, 0]
    print(distinct_numbers(my_list)) # [1, 2, 3]
    print(distinct_numbers(my_list1))