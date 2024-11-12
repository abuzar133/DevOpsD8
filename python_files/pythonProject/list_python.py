list_of_names = ["mateen","mohammed","talha", "amair", "abuzar", "messi"]
                # 0           1         2        3       4         5
                # -6          -5          -4         -3        -2         -1

list_random_data = ["apple", 13 , 17.0]
#lists are hetrogenous
#lists are mutable
#list are also sequences
#lists can include integer variable float any values together as seen in line n0 5

print(list_of_names[2])
list_of_names[2] = "Ronaldo"
print(list_of_names)
print(list_of_names[4])
print(list_of_names[-1])

#slicing
print(list_of_names[::])

#stepslicing pending

#nested lists
lists_nested = [1,2,3,[4,5,6]]
lists_nested1 = [["mateen","abuzar"], [45,67],10,12]
print(lists_nested1[1][1])
print(lists_nested1[0][1][3])

lists_random_data = [["apple", ["iphone15", "airpods","macbook pro m3"]],
                     ["samsung",["S24 ultra", "Earpods", "tab"]]]
print(lists_random_data[0][1][1]) #airpods
print(lists_random_data[1][1][2]) #tab

#lists builts in
#mutable objects
#append method
l = [1,2,3]
l.append(4)
print((l))

#pop method
l = [1,2,3]
l.pop() #will remove the last element from the list
print(l) #[1,2]
l.pop(0)
print(l) #2

#reverse a alist

l = [1,2,3]
l.reverse()
print(l)

#count method -  to give  COUNT of elementd in a given list
l = [1,1,2,2,3,3]
print(l.count(2)) #2 - since 2 is occuring 2 times in the list

l = ["a","a","b","b","c","c","d"]
print(l.count("a")) #3 since "a" is ocurring 3 times in a alist
my_list = []

#insert - insert an elemnet at given index posiition
my_list = [1,2,3]
         # 0,1,2
my_list.insert(1,'a') # (1,'a',2,3)
print(my_list)

#remove - remove an element from the list
my_list = ["a","b","c","d"]
my_list.remove("c")
print(my_list)

#sort method
my_list= [1,4,7,2,9,0]
my_list.sort() #asc order - lower tpo higher
print(my_list)

my_list.sort(reverse=True)  #desc order
print(my_list)

# what is the difference between shallow copy and deep copy

#shallow copy
l1 = [1,2,3,4,5]
l2 = l1.copy()  #shallow copy
l1[0] = 100
print(l1)
print(l2)
l1 = [[1,2,3,] , [4,5,6] , [7,8,9]]
l2 = l1.copy()
print(l2)
l1[0][0] = 100 # changing in l1 will reflect in l2 as well because of shallowcopy as shallow copy refers to the same object as original list

# deep copy
import copy
l1 = [1,2,3,4,5,]
l2 = copy.deepcopy(l1)
print(l1)
print(l2)

l1 = [[1,2,3],[4,5,6],[7,8,9]]
l2 = copy.deepcopy(l1)
l1[0][0] = 100 #change in l1 will not reflect l2 as deep copy creates completely new independent object
print(l1)
print(l2)
