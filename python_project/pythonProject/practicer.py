#conditional if else
age = 18
if age < 18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")

age = 18
if age <= 18:
    print("you are eligible for voting")
else:
    print("ypu are not eligible for voting")

age = 25
if age < 13:
    print("you are a child")
elif age > 13 and age < 18:
    print("you are a teenager")
elif age > 18 and age < 65:
    print("you are an adult")
else:
    print("you are senior citizen")

marks = 95
if marks > 95:
    grade = "A"
elif 85 < marks < 75:
    grade = "B"
elif 75 < marks < 65:
    grade = "C"
elif 65 < marks < 55:
    grade = "D"
else:
    grade = "F"
print(grade)

credit_score = 990
if credit_score <= 760:
    score = "good"
elif (credit_score < 760) and (credit_score > 660):
    score = "average"
elif (credit_score < 660) and (credit_score > 560):
    score = "below AVERAGE"
elif (credit_score < 560) and (credit_score > 460):
    score ="bad"
else:
    credit_score < 460
    score = "very bad "
print(score)

account_active = False
account_balance = 10_000
withdrawal_amount = 5_000
if account_active and withdrawal_amount <= account_balance:
    remaining_balance = account_balance - withdrawal_amount
    print("withdrawal completed")
    print(remaining_balance)
else:
    print("withdrawal declined")




credit_score = int(input("enter you credit score"))
if credit_score > 0 and credit_score < 580:
    score = "poor"
elif credit_score > 580 and credit_score < 670:
    score = "fair"
elif credit_score > 670 and credit_score < 740:
    score = "good"
elif credit_score > 740 and credit_score < 800:
    score = "very goood"
else:
    credit_score > 800 and credit_score < 850
    score = "excellent"
print(score)

#nested elif
age = 8
if age < 10:
    print("child")
    if age < 10 and age > 4:
        print("naughty")
    elif age > 4:
        print("just born")
    elif age < 10:
        print("school kid")
else:
    print("mature person")


