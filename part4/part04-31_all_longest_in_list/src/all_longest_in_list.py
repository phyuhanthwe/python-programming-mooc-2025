# Write your solution here
def all_the_longest(l):
    max_len = len(max(l, key=len))
    return [s for s in l if len(s) == max_len]

if __name__=="__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
