#lamda functions are anonymous functiuons that are defined using lambda keyword
#small operations that can be defined in a single line
def add_nums(a,b):
    return a + b

l = lambda a, b : a + b
print(l) # l is a function pointing towards lambda functionaddress in memory
print(l(5,10))

def sq_num(num):
    return num ** 2

f = lambda num : num ** 2
print(f(5))

#write a lambda function check its even or not

def check_even(num):
    if num % 2 == 0: #true or false
        return True
    else:
        return False


#write a lambda function check its even or not . with lambda function

l = lambda num : num % 2 == 0
print(l(4))

f = lambda s : s.upper()
print(f("abdul"))

#write a lamda function that should return sum of 3 numbers

def sum_of_nums(a,b,c):
    return a+b+c
sum_of_nums(2,4,6)

f = lambda a,b,c : a + b + c
print(f(1,2,3))

#maps & filters in lambda function
#maps applies a function to all thr items in an input list
def sq_num(list_nums):
    output_list = []
    for n in list_nums:
        output_list.append(n ** 2)
        return output_list

sq_num_list = sq_num([1,2,3,4,5,])
print(sq_num_list)


# using map function

l = [1,2,3,4,5]
f = list(map(lambda n : n ** 2 ,l))
#'' here we are converting squarte of the given list using map function which itrerates over each number in the list''
print(f)

l =[ "a", "b", "c", "d","e","f"]
def upper_case_list(list_chars):
    output_list = []
    for char in list_chars:
        output_list.append(char.upper())
    return output_list

l = upper_case_list(["a", "b", "c", "d", "e", "f"])
print(l)

#using map function
l = ["a", "b", "c", "d", "e", "f"]
f = list(map(lambda c: c.upper(),l))
#''' here we are connverting given list in to upper case using map function anmd builtin .upper'''
print(f)

#filter function
#filter function filtersthe given list based on the condition given in the lambda function

l = [1,2,3,4,5,6]
def check_even(list_num):
    output_list = []
    for num in list_num:
        if num % 2 == 0:
            output_list.append(num)
    return output_list

l = check_even([1,2,3,4,5,6])
print(l)

#Using Filter function
l = [1,2,3,4,5,6]
f = list(filter(lambda n: n % 2 == 0, l))
#''' here we are filtering the given list to find the even number in given list'''
print(f)

list_strings = ["abdul", "mateen", "abc", "ff", "l"]
def filtered_strings(list_strs):
    output_list = []
    for s in list_strs:
        if len(s) > 2:
            output_list.append(s)
    return output_list

l = filtered_strings(["Abdul", "mateen", "Abc", "Ff", "L"])
print(l)


list_strs = ["Abdul", "mateen", "Abc", "Ff", "L"]
list_filtered_strs = tuple(filter(lambda s: len(s)> 2, list_strs))
#'''here we are filtering the string whose length is greater than 2 in the given list'''
print(list_filtered_strs)

list_filtered_upper = list(filter(lambda s: s[0].isupper(), list_strs))
print(list_filtered_upper)



