#while loops are the loops in which iteration goes on until the exit conditon has been met
print("exmple")
i = 0
while i < 10 : #0< less than 10 true
    print(i)
    i = i + 1 #0 +1 = 1 it goe untill 10<10 occurs which is false and exit condition to the loop if there is no exit condition the loop goes on and never stops

print("##############33break###################33333333")

l = [1,2,3,4,5,6,7] #here i want iteration untill 4 i can use break like this by using condition at ln no 14
for num in l :
    if num % 2 == 0:
        print(f"{num}is even")
        if num == 4:
            break # abnormally break the loop and stop iteration

i = 0
while i < 10:
    print(i)
    i = i + 1
    if i == 7:
        break

#####################################continue#####################

i = 0
while i < 10:
    print(i)
    i = i + 1
    if i == 7: # whn condition i ==7 is false condition met it wont execute the below code for that iteration after 6 as in output ad goes on with next iteration
        continue
    print(f"some code executed")
    print(f"some more code been executed")
    a = 1
    b = 2
    c = a+b
    print(c)
