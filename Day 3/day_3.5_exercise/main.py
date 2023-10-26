# Love Calculator exercise

print("Welcome to the Love Calculator!!!!")

name1 = input("What is your name?   ")
name2 = input("What is their name?   ")

combined_name = name1 + name2
lower_case_string = combined_name.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)
love_score_as_int = int(love_score)

if (love_score_as_int < 10) or (love_score_as_int > 90):
    print(f"Your love score is {love_score_as_int}, you go together like coke and mentos.")
elif (love_score_as_int >= 40) or (love_score_as_int <= 50):
    print(f"Your love score is {love_score_as_int}, you are alright together.")
else:
    print(f"Your love score is {love_score_as_int}")
