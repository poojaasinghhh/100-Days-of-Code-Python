# input for year

year = int(input("Which year do you want to check:    "))

# checking if year is leap year or not

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")
