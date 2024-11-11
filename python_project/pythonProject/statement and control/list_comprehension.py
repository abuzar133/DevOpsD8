list_nums = [1,2,3,4,5,]
#list_sq_nums = [1,4,9,16,25]
#conventional method
list_sq_nums = []
for num in list_sq_nums:
    list_sq_nums.append(num ** 2)
print(list_sq_nums)

#list comprehension method
list_nums = [1,2,3,4,5,]
list_sq_nums_comp = [num ** 2 for num in list_nums]
print(list_sq_nums_comp)

strings = 'Pyhton is an awesome language'
list_of_strings = strings.split(" ")
# output = ['python', 'is', 'an' ,'awesome' ,'language']

print(list_of_strings)
#conventional method
filtered_list = []
for word in list_of_strings:
    if len(word) >= 5:
        filtered_list.append(word)
#comprehension method
filtered_list_comp = [word for word in list_of_strings if len(word) >= 5]

#dictionary comprehenshion

list_nums = [1,2,3,4,5]
#output_dict = {1:1,2:4,3:9,4:16,5:25}

#conventional method
output_sq_dict = {}
for num in list_nums:
    output_sq_dict[num] = num ** 2 # add key value pair to dictionary
print(output_sq_dict)

#dictionary comprehension
list_nums = [1,2,3,4,5]
output_sq_dict = {k:k ** 2 for k in list_nums}
print(output_sq_dict)

######interview question  #########

strings = "aaabbbcccdddeeef"
#{a :3, b :3, c: 3, d: 3 e:3}
char_count = {} #{'a': 3, 'b' : 3, 'c':3}
for char in strings:
    if char in char_count.keys():
        char_count[char] = char_count[char] + 1 #char count ['a'] + 1 = 3
    else:
        char_count[char] = 1 #char_count ['b'] = 1 {'a' : 3 , 'b' :3, 'f' :1}
    print(char_count)