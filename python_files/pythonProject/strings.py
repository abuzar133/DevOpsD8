my_name = "abuzar"
print(type(my_name))

my_first_name = "Mohammed"
my_second_name = "Abuzar"
my_name = "@buzar"
print(my_second_name)
print(my_name)

#strings are immutable
my_name = "Abuzarkhan"
my_name = ("abdulkareem")
            #0123456789    #positional index
            #          -3-2-1 negative index

print(my_name[-1])




#methods  donated bt{.}
my_name = " mdabuzar "
print(my_name.capitalize())
print(my_name.upper())
print(my_name.lower())
print(my_name.strip())
print(my_name.lstrip())
print(my_name.rstrip())

my_string = "--hello world--"
print(my_string.strip("-"))
text = "hello world"
print(text.replace("world","there"))


text = "hello-world"
print(text.split("-"))

print(text.startswith("h"))  #checks the starting alphabet and says true or false
print(text.endswith("e")) #checks the ending alphabet and says true or false

print(text.isupper()) #will the if the string value is in completely upper case _ reterun boolean valuye true or false
print(text.islower()) #will the if the string value is in completely lower case _ reterun boolean valuye true or false

age = ('1a2b3c')
print(age.isnumeric()) #will check the string value is completely in numerical return boolean value true or false
print(age.isalnum())  #will check the string value is completely in alpha numerical return boolean value true or false