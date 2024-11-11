#list_num = [1,2,3,4,5,6,7,8]
#list_squared_num = [1,4,6,15,25,36,49,64]

#you have been given a list of integers
#expectation is to create another list with the squares of the number from the given list

list_num = [1,2,3,4,5,6,7,8,]

#intialize an outpput list
list_sq_num = []

#itreate over given list and calculate square of each number and append to the intilalized list
for num in list_num:
    list_sq_num.append(num ** 2) #[1,4,9,16,25,36,49,64]
print(list_sq_num)



#given list
list_num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
#expectation is for each number, if the number is odd, it should print the nmumber and "odd"
#if the number is even, it should print the number and "even"

#iterate over the given list, check if the each number when divided by 2
#if the remainder is 0 ,if true,print even ,if false,print odd
for num in list_num:
    if num % 2 ==0: #if 3 % 2 ==0 -> false
        print(f"{num}is even")
    else:
        print(f"{num}is odd")



#list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Expectation = [3, 4, 5, 6, 7, 8, 9, 10, 11, 13] Add 2 to each number from original list and append to the output list

list_of_num =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_of_num_plus2 = []

for num in list_of_num:
    list_of_num_plus2.append(num + 2)

print(list_of_num_plus2)

#nested lists, Nested tuples
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
for main_list in nested_list:
    for num in main_list:
        print(num)

#nested list but with one element as non iterable element
nested_list = [[1,2,3],[4,5,6],7]
for sub_list in nested_list:
    if isinstance(sub_list,list): # we aree checking if sublist is list of data typr , onlythen we are iterating
        for num in sub_list:
            print(num)
    else:
        print(sub_list)

#iterabales are only collection of numbers or elements ex are
#strings
#lists
#tuples
#dictionaries
#sets
#theses are called iterables


nested_list = [[1,2,3],[4,5,6],("a", "b" ,"c") ,7]
for sub_list in nested_list:
    if isinstance(sub_list,(list, tuple)): # we aree checking if sublist is list of data type or tuple , onlythen we are iterating
        for num in sub_list:
            print(num)
    else:
        print(sub_list)


#flattening lists
list_num = [1,2,3,4,5,[6,7,8],(9,10,11),12,13]
#expected output = [1,2,3,4,,5,6,7,8,9,10,11,12,13]

#intialize output list
#most asked interview question ################################33
flatten_list = []
for num in list_num: #num = 6,7,8
    if isinstance(num,(list,tuple)):
        flatten_list.extend(num)
    else:
        flatten_list.append(num)
print(flatten_list)


dict_1 = {"a": 1, "b": 2, "c": [3,4,5,6]}
for key, value in dict_1.items():
    print(key)
    print(value)

#Iterate over the list and print each element, modify the above program to do so

dict_1 = {"a": 1, "b": 2, "c": [3,4,5,6]}

for key,value in dict_1.items():
    if isinstance(value,list):
        print(key)
        for num in value:
            print(num)
    else:
        print(key)
        print(value)


#iteration using range
print("Iteration using range function ")
list_num = [1,2,3,4,5,6,7,8]
           #0 1 2 3 4 5 6 7
for i in range(0,len(list_num)): #range(0,8) -> 0,1,2,3,4,5,6,7 i: 7
    print(list_num[i])

list_num = [2,4,3,7,9,0,-2,11,-4,5]
#question is if sum of any two numbers from the list == 7 -> print indexesof any two such numbers
for i in range(0,len(list_num)):
    for j in range (i+1 , len(list_num)):
        if list_num[i] + list_num[j] == 7:
            print([i,j])
            






