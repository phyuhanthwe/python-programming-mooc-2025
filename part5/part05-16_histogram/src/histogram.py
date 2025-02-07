# Write your solution here
def histogram(str):
    d = {}
    for i in str:
        if i not in d:
            d[i] = 0
        d[i] += 1
    for k, v in d.items():
        s = f"{k} {'*' * v}"
        print(s)

if __name__=="__main__":
    (histogram("abbc"))