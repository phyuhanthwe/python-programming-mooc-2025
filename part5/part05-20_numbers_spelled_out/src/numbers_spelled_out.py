# Write your solution here
def dict_of_numbers():
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    number_dict = {}
    
    for i in range(100):
        if i < 10:
            number_dict[i] = ones[i]
        elif 10 <= i < 20:
            number_dict[i] = teens[i - 10]
        else:
            ten_part = tens[i // 10]
            one_part = ones[i % 10] if i % 10 != 0 else ""
            number_dict[i] = ten_part + ("-" + one_part if one_part else "")
    
    return number_dict