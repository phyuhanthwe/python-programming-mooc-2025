# Write your solution here
def replace():
    l = [1, 2, 3, 4, 5]
    while True:
        i = int(input("Index: "))
        if i == -1:
            break
        else:
            v = int(input("New value: "))
            l[i] = v
            print(l)
replace()
