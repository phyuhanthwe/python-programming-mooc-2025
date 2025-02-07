# Write your solution here
def times_ten(a, b):
    d = {}
    for i in range(a, b+1):
        d[i] = i * 10
    return d

if __name__=="__main__":
    d = times_ten(3, 6)
    print(d)
