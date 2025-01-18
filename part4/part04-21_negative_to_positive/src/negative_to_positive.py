# Write your solution here
def neg_to_pos(a):
    for i in range(-a, a+1):
        if i != 0:
            print(i)

num = int(input("Please type in a positive integer: "))
neg_to_pos(num)