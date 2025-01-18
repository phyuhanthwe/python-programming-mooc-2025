# Write your solution here
def anagrams(a, b):
    sort_a = sorted(a)
    sort_b = sorted(b)
    if sort_a == sort_b:
        return True
    else:
        return False
    
if __name__=="__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java"))