# Program to add digits in a two-digit number.

# Input: 23 Output:5(2+3)

two_digit_number = input("Type two digit number. \n")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)

print(result)
