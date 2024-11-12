age = 18
#Indentation
#conditional statements
if age >= 18:
    print("you are eligible for voting") #the front gap is called indentation

else:
    print("you are not eligible for voting")


age = 66

if age < 13:
    print("you are a child ")
elif (age > 13) and (age < 18):
    print("you are a teenager")
elif (age > 18) and (age < 65):
    print("you are an adult")
else:
    print("you are a senior citizen")

marks = 45
if marks >= 95:
    grade = "A"
elif 85 < marks < 95:
    grade = "B"
elif 65 < marks < 85:
    grade = "C"
elif 55 < marks < 65:
    grade: "D"
else:
    grade ="F"
print (grade)

account_active = True #boolean values
account_balance = 10_000 #integer
withdrawal_amount = 5_000 #integer
if account_active and withdrawal_amount <= account_balance:
   remaining_balance = account_balance - withdrawal_amount
   print("withdrawal completed")
   print("remaining_balance")
else:
    print("withdrawal declined")
 ##

 #nested elif if 
age = 7
if age >= 0:
    if age < 13:
        print("child")
        if age > 5 and age < 8:
            print ("naughty")

    elif age < 20:
        print ("teenager")
    elif age < 65:
        print ("adult")




