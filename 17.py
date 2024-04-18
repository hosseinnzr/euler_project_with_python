def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundred = "hundred"
    thousand = "thousand"

    if n == 1000:
        return "onethousand"

    words = ""
    if n // 100 > 0:
        words += ones[n // 100] + hundred
        if n % 100 == 0:
            return words
        else:
            words += "and"
    if n % 100 // 10 == 1 and n % 10 != 0:
        words += teens[n % 10]
    else:
        words += tens[n % 100 // 10]
        words += ones[n % 10]
    return words

total_letters = 0
for i in range(1, 1001):
    total_letters += len(number_to_words(i))

print(total_letters)

# result : 21124
