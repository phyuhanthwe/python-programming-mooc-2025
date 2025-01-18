# Write your solution here
def first_word(s):
    l = s.split(" ")
    # if len(l) >= 3:
    return l[0]

def second_word(s):
    l = s.split(" ")
    # if len(l) >= 3:
    return l[1]
    # else:
    #     return l[0]

def last_word(s):
    l = s.split(" ")
    return l[-1]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))

    sentence1 = "happily ever after"
    print(first_word(sentence1))
    print(second_word(sentence1))
    print(last_word(sentence1))

    sentence2 = "first second"
    print(first_word(sentence2))
    print(second_word(sentence2))
    print(last_word(sentence2))
