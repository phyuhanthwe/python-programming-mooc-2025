# Write your solution here
def longest_series_of_neighbours(l):
    max_len = 1
    curr_len = 1
    for i in range(1, len(l)):
        if abs(l[i] - l[i-1]) == 1:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1
    return max_len

if __name__=="__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))