# Write your solution here
def no_shouting(l):
    result = []
    for i in l:
        if not i.isupper():
            result.append(i)
    return result

if __name__=="__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)