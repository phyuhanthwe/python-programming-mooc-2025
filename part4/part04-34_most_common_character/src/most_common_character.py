# Write your solution here
from collections import Counter
def most_common_character(s):
    frequency = Counter(s)
    return max(frequency, key=frequency.get)

if __name__=="__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))