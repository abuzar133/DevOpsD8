#range function SESSION 14 RECORDING 1
#its memory efficient
#it uses less memory than the list and we write range(100) it doesnt store 100 numbers in the memory space its generates number on the fly
#list [1,3,4,4,5] lists store the numbrs in the memory
#range(20) its means (0............19)n-1 concept is used
#main thing is after writing the range function when we need range of valuess first we need to convert them into list object as done in line no 11,17

list1 = [1,2,3,4,5,6,7,8,9]
my_numbers = range(10)
print(my_numbers)
listl1 = list(my_numbers)
print(listl1)

my_numbers = range(0,10,3)
listl2 = list(my_numbers)
print(listl2)
print(list(my_numbers))
mynums = range(65)
print(list(mynums))
print(tuple(mynums))

list1 = [1,2,3,4,5,5,6,6,]
mynums = range(20)
print(mynums)
print(list(mynums))
mynums1 = range(0,20,3)
print(list(mynums1))


#for loop SESSION 15 RECORDING 2

string_name = "ABUZAR"
for char in string_name:
    print(char)
    print("iteration is going on")
print("iteration is completd")

#list for loop execution
print("list for loop execution")
listl4 = ["abuzar","khan",55,66, [1,2,4,], (4,5,6), {"a": 1,"b": 2}]
for data in listl4:
    print(data)
#tuple for loop execution
print("tuple for loop execution")
tuplet4 = ("abuzar","khan",55,66, [1,2,4,], (4,5,6), {"a": 1,"b": 2})
for elements in tuplet4:
    print(elements)
print("ITERATION COMPLETED")

print("USING BUIT-INS IN LOOPS")
print("upper builtin ")
#convert the given string into upper case
listofnames = ["abuzar","mubeen","amair","farhan","nahid"]
for char in listofnames:
    print(char.upper())
for char in listofnames:
    print(char.lower())

#print
listofnamesl1 = ["mubeen","amair","abuzar","khan","mudassir","arshad"]
for data in listofnamesl1:
    print(data[0])

print("LOOPS FOR DICTIONARIES")
dict_1 = {"a":1, "b":2, "c":3, "d":4}
for key,value in dict_1.items(): #.items is dictionary builtin used for getting both key and values
    print(key)
    print(value)
print("ONLY KEYS")
for key in dict_1.keys():
    print(key)
print("only values")
for values in dict_1.values():
    print(values)
