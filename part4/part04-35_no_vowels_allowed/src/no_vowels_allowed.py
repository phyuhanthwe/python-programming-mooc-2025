# Write your solution here
def no_vowels(s):
    vowels = "aeiou"
    no_vowels_s = ""
    for i in s:
        if not vowels.__contains__(i):
            no_vowels_s += i
    return no_vowels_s

if __name__=="__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))