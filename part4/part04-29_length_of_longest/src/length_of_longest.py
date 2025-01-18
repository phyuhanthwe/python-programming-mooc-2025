# Write your solution here
def length_of_longest(l):
    length = []
    for i in l:
        length.append(len(i))   
    return max(length)

if __name__=="__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)