#for loops - iteration mechanism
#A for loop iterates over an iterable

string_name = "abuzar"
for char in string_name:
    print(char)
    print("iteration is going on")

print("iteration is completed")

print("list for loop execution")
list_random = ("abdul" , "mateen" , 7, 8.99 ,[1,2,3,], (7,8,9),{"a":1, "b":2})
for data in list_random:
    print(data)

print("tuple for loop execution")
tuple_random = ("abdul" , "mateen" , 7, 8.99 ,[1,2,3,], (7,8,9),{"a":1, "b":2})
for data in tuple_random:
    print(data)

#convert the string in given list to upper case

list_name = ["abdul", "mateen" , "abuzar","mubeen","farhan","amair"]
for name in list_name:
    print(name.upper())

#Print the first character of each string from the given list of strings
list_names = ["abdul", "mateen", "abuzar", "mubeen", "farhan","amair"]
for name in list_name:
    print(name[0])

dict_1 = {"a": 1, "b": 2,"c":3}

for k,v in dict_1.items(): #itreate over key , value pairs
    print(k)
    print(v)


for k in dict_1.keys(): #iterate only over keys
    print(k)

for v in dict_1.values(): #iterate over only values
    print(v)


