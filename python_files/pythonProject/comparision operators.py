a = 2

a = 5  #if the values are different output is false
b = 5
#comparision opertors --> yield boolean values -> true or false
print (a == b) # will compare value of tge variable - object
print (a is b) # it will checck if both a and b are resided in the same location
print (id(a), id(b))

 #but in listing value its different

a = [1,2,3]
b = [1,2,3]
print (a == b)
print(a is b) #memory location is different so false

print ("**********************************")
#not equal to
num1 = 100
num2 = 200
print(num1 != num2)  ##the middle used sign is not equal to sign in python

print("***********************************")
#greater than and greater than amd equal to
num1 = 100
num2 =200
print(num1 > num2)
print(num1 >= num2)

print("#############################")

#lesser than lesser than or equal to
num1 = 100
num2 = 200
print(num1 < num2)
print(num1 <= num2)








