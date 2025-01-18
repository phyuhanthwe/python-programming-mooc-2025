# Write your solution here
def add():
    l = []
    num_of_items = int(input("How many items: "))
    for i in range(num_of_items):
        a = int(input(f"Item{i+1}:"))
        l.append(a)
    print(l)

add()