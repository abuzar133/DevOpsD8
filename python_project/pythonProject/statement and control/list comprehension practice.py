#list comprehension
#conventional ,method
list_nums = [1,2,3,4,5] # we need square of this list
listsq_nums = []
for num in list_nums:
    listsq_nums.append(num **2)
print(listsq_nums)
print("this can be writeen in list comprehension in this way")
list1 = [1,2,3,4,5]
listsq_numscomp = [num **2 for num in list_nums]
print(listsq_numscomp)

list1 = [1,2,3,4,5,6,7]
listplus_comp = [num + 2 for num in list1]
print(listplus_comp)

print("string comprehension")
strings = 'Python is an awesome language'
list_of_strings = strings.split(" ") # as we use this buitin the output returned will be in list format as see in line no 58
print(list_of_strings)
#output = ['Python', 'is', 'an', 'awesome', 'language']
#in this i need words which are greater than 5
#conventional method
filtered_list = []
for word in list_of_strings:
    if len(word) >= 5:
        filtered_list.append(word)
print(filtered_list)

# list comprehension
filtered_list = [word for word in list_of_strings if len(word) >= 5]
print(filtered_list)


