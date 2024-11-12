#strings "" , '' , """ """ , ''' '''
#strings are squences they have indexes
#strings are immutable


my_name = "abuzar"
#index     012345
print(my_name)

#strings can be sliced
my_name = "Mohammed"
#indexes   01234567
print(my_name[1])

#slicing concepts
my_name = "Mohammed"
print(my_name[0:5])
print(my_name[:6])
print(my_name[2:6])  # 2,3,4,5,  (n-1) concept
print(my_name[:6])  # 0,1,2,3,4,5
print(my_name[3:])  # 3,4,5,6,7
print(my_name[:]) #start to end

# step slicing
my_name = "Mohammed"
#need every second element
print(my_name[::2])

#negative slicing
my_name = "Mohammed"
print(my_name[-1])
print(my_name[:-1])
#revrse
print(my_name[::-1])

#built ins (.)
my_name = " Mohammed "
print(my_name.upper())
print(my_name.lower())
print(my_name.strip())
print(my_name.lstrip())
print(my_name.rstrip())

my_string = "--helloworld--"
print(my_string.strip("-"))

text = "hello world"
print(text.replace("world","there"))
print(text.startswith("h"))
print(text.endswith("l")) # return boolean values true or false
print(text.isupper())
print(text.islower())

#stings interpoliation ND strings concatenation pending

#LISTS
#lists are mutable
#lists are squences
#indicated by []
l= [1,2,3,4,5]
print(type(l))

#Mutability
l = ["abdul", 123, 8.9, [1,2,3], {"a": 1, "b": 2}]
    #0          1   2      3         4
print(id(l))
print(l[0])
l[0] = "kareem"
print(l)
print(id(l))
#changing of elements with same memory location

#slicing
l = ["abdul", 123, 8.9, [1,2,3], {"a": 1, "b": 2}]
    #0          1   2      3         4

print(l[0:3])
print(l[:3])
print(l[2:5])
print(l[::2])
#similarly negative slicing

#built in methods
l = ["abdul", 123, 8.9, [1,2,3], {"a": 1, "b": 2}]
    #0          1   2      3         4
#want to replce 123 with 1000
print(l.insert(1,1000))
print(l)
print(l.append(2))
print(l) # adding a element to the list
print(l.pop(3))

#pop
my_list = [1,2,4,4,4,5,6]
print(my_list.pop())
print(my_list)

#count
list = [1,1,2,2,3,3,3,4,4,5,6]
print(list.count(3))
print(list)

#sort
list = [1,2,3,4,5,6,7,8]
print(list.sort()) #asc oirder
print(list)
#reverse
print(list.sort(reverse=True))  #desc order
print(list)

#extend
l = [1,2,3,4,5,6]
l1 =[7,8,9,10]
print(l.extend(l1))
print(l)

#remove
l=[1,2,3,4,4]
print(l.remove(4))
print(l)

#clear
l=[1,2,3,4,4]
print(l.clear())
print(l)

#copy
l=[1,2,3,4,4]
print(l.copy())
print(l)

#tuples
#()
#Sequence
#Immutable
t = ('a','b','c','d')
    # 0    1   2   3
t = ([1,2,3], {'a':1, 'b':2}, 123, "abdul", 7.9, False)
     #0 1 2
    #   0            1         2       3     4    5
print(id(t))
print(t[0].append(100))
print(t)
print(id(t))
#Immutable

#builtins
print(t.index("abdul"))

