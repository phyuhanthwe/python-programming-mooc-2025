# Write your solution here
def same_word_twice():
    l = []
    while True:
        word = input("Word: ")
        if word not in l:
            l.append(word)
        else:
            break
    print(f"You typed in {len(l)} different words")
 
same_word_twice()