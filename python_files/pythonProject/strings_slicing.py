my_text = "Hello world"
          #01234
print(my_text[0])
print(my_text[0:5]) #it will print all 4 , 5 is exclusive n-1 is used
print(my_text[:5])
print(my_text[:])
print(my_text[3:7])

#negative slicing

city = "Hyderabadi"   #slicing always move from left to right
      #012345678
      #-9      .-1  #negative slicing
print(city[-5:-1])
#step slicing

city = "Hyderabadi"
print(city[0:10:2])
print(city[::2])
print(city[::3]) #every third element starting from 0th index
print(city[1::3]) #starting point and ending point are inclusive
print(city[-10::-2]) #same as city [0:10:2] but using negative index

#reverse a string
city = "Hyderabad"
print(city[::1]) #prints reverse string -1 will consider steps in neagative direction - from right to left


#Concantenation

First_name = "Abuzar"
Last_name = "Mohammed"
print(First_name+" "+Last_name)

age = 28.5
print(type(age))

str_age = str(age)  #type casting -int age converted to string age
print(type(str_age))

print(("my_age+is"+str(age))

age= 25
ID = 14177
salary = 10_000
name = "abuzar"
statement  ="my name is name ",My_Emp_ID is"+str(id)+"My_age_is"+str(age)+"my_salary is +str(salary)
print(statement)

#f strings _ formatted string
statement = f"my name{name}.My EmpID is {ID}.My age is {age} My Salary is {salary}."