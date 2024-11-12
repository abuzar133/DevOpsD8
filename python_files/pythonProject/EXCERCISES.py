elapsed = 7835 #1 min = 60 seconds , 1 hour = 60 mins so to get hours we do (60 * 60)
hours = 7835 // (60 * 60 ) # this will give hour value
print(hours)
remaining_seconds = 7835 % (60 * 60) #remaining seconds after taking out hour component
minutes = remaining_seconds // 60 # minutes component from remaining seconds
print(minutes)
seconds = remaining_seconds % 60 #remaining seconds # remaining seconds after taking out minutes component
print(seconds)

# excerise 2
a = None  #none value - basically no value - just a place holder in memory
if a == None:
    a = "N/A"
else:
    a = a
print(a)

#ternarey operator
a ="N/A" if a == None else a
print(a)

# EXCERCIS 3
credit_score = int(input("enter you credit score"))
if credit_score > 0 and credit_score < 580:
    rating = "poor"
elif credit_score >= 580 and credit_score< 670:
    rating = "fair"
elif credit_score >= 670 and credit_score < 740:
    rating = "Good"
elif credit_score >= 740 and credit_score < 800:
    rating = "very good"
elif credit_score >= 800 and credit_score <= 850:
    rating ("excellent")
print(rating)

#excersie 4
a = int(input("Enter a number:"))
if a % 2 == 0:
    print(f"The number {a} is even")
else:
    print(f"The number{a}is not even")


 #excercise 5
list_of_phones = ["apple", "samsung", "Blackberry", "google", "nokia"]
print(list_of_phones[0][2])
print(list_of_phones[2][5])
print(list_of_phones[4][4])