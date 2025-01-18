# Write your solution here
def star_studded(s):
    new_s = ""
    for i in s:
        # new_s += i + "*"
        print(i)
        print("*")

    print(new_s)

user_input = input("Please type in a string: ")
star_studded(user_input)
