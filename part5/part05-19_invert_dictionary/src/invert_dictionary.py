# Write your solution here
def invert(d):
    v = list(d.values())
    k = list(d.keys())
    d.clear()
    return d.update(dict(zip(v, k)))

if __name__=="__main__":
    # s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    s = {1: 10, 2: 20, 3: 30}
    invert(s)
    print(s)