# Write your solution here
def everything_reversed(l):
    l = l[::-1]
    reverse_list = []
    for i in l:
        reverse_list.append(i[::-1])
    return reverse_list

if __name__=="__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)