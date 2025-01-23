# Write your solution here
def add_removal():
    l = []
    print("The list is now []")
    i = 1
    while True:
        word = input("a(d)d, (r)emove or e(x)it: ")
        if word == "d":
            l.append(i)
            i += 1
            print(f"The list is now {l}")
        if word == "r":
            l.pop()
            i -= 1
            print(f"The list is now {l}")
        if word == "x":
            print("Bye!")
            break
 
add_removal()