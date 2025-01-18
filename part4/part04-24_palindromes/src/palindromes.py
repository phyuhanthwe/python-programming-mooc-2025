# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

while True:
    s = input("Please type in a palindrome: ")
    def palindromes(s):
        return s == s[::-1]
    if palindromes(s):
        print(f"{s} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

# if __name__ == "__main__":
#     palindromes("neveroddoreven")