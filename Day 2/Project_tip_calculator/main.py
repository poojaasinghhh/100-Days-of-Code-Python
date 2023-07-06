# Day 2 project - Tip calculator

print("Welcome to the Tip Calculator.")

bill = input("What was the total bill? $")
bill_as_float = float(bill)

tip = input("How much tip would you like to give? 10, 12 or 15? ")
tip_as_int = int(tip)

people = input("How many people to split the bill? ")
people_as_int = int(people)

bill_with_tip = tip_as_int / 100 * bill_as_float + bill_as_float

bill_per_person = bill_with_tip / people_as_int

total_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay ${total_amount}.")
