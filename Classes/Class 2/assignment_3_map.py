# dictionarys for words
ones = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
}

teens = {
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
}

tens = {
    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
    60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
}


def num_to_words(n):
    if n < 10:
        return ones[n]
    elif 10 <= n < 20:
        return teens[n]
    elif n < 100:
        if n % 10 == 0:
            return tens[n]
        else:
            return tens[n - n % 10] + "-" + ones[n % 10]


nums = [10, 15, 30, 42, 55, 60, 75, 53, 99]

letter_form = list(map(lambda x: num_to_words(x), nums))

print("Assignment 3:", letter_form)