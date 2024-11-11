l = [1,2,3,4,5,6,7,8]
#create an expected output squared of list [1,4,9,16,25,36,49,64]

listofsqnum = []
for num in l:
    listofsqnum.append(num ** 2)
print(listofsqnum)

       #OR

l = [1,2,3,4,5,6,7,8]

for num in l:
    sq_num = num ** 2
    listofsqnum.append(sq_num)

print("loops usimng conditionals if else")

l = [1,2,3,4,5,6,7,8,9]
#expected if the numm is odd print odd if the num is even print even

for num in l:
    if num % 2 == 0:
        print(f"{num}is even")
    else:
        print(f"{num} is odd")

print("example problem")
l = [1,2,3,4,5,6,7,8]
#expectation is l2 = [adding 2 to given list]
#output = [3,4,5,6,7,8,9,10]

listofnumplus2 = []
for num in l:
    listofnumplus2.append(num + 2)
print(listofnumplus2)

print("NESTED LISTS AND NESTED TUPLES")
l = [[1,2,3],[4,5,6],[7,8,9]]
for main_list in l:
     print(main_list)

#we need 1,2,3 in nested list separate we write 2 for loops because we got nested list
for main_list in l:
    for num in main_list:
        print(num)

l = [[1,2,3],[4,5,6],7]
#iteration is only done is sequence of elements like lists, tuples but here 7 is an integer which is not iterable so how do we handle this case


#here only lists and sublist are bbeing printed 7 is not printed because its not iterable now we can handle that using if else conditionals

print("nested list with an integer")
nested_list = [[1,2,3],[4,5,6],7]

for sub_list in nested_list:
    if isinstance(sub_list,list):
        for num in sub_list:
            print(num)
    else:
        print(sub_list)

print("nestedlist with a tuple ")

nested_list = [[1,2,3], [4,5,6], ("a","b","c"), 7]
for sub_list in nested_list:
    if isinstance(sub_list,(list,tuple)): # group them together as shown in this line
        for num in sub_list:
            print(num)
    else:
        print(sub_list)

print("flatennig list")
list_num = [1,2,3,4,5,[6,7,8],[9,10,11],12,13]
#expected output = [1,2,3,4,5,6,7,8,9,10,11,12,13]
flattening_list = []
for num in list_num:
    if isinstance(num,list):
        flattening_list.extend(num)
    else:
        flattening_list.append(num)

print(flattening_list)

dict_1 = {"a": 1,"b": 2,"c":[3,4,5,6]}
for key,value in dict_1.items():
    if isinstance(value,list):
        print(key)

        for num in value:
            print(num)
    else:
        print(key)
        print(value)
