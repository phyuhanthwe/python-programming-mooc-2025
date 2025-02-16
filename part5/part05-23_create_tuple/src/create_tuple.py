# Write your solution here
def create_tuple(x, y, z):
    lst = [x, y, z]
    tup = (min(lst), max(lst), sum(lst))
    return tup

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))