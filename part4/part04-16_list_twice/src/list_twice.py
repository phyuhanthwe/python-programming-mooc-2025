# Write your solution here
def list_twice():
    l = []
    while True:
        num = int(input("New item: "))
        if num == 0:
            print("Bye!")
            break
        else:
            l.append(num)
            print(f"The list now: {l}")
            print(f"The list in order: {sorted(l)}")
 
list_twice()
