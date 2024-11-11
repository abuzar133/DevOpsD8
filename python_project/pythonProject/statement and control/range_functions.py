#range functions
#integers between certain range

list_1 =[0,1,2,3,4,5,6,7,8,9,10] # creates a place holder for list object
my_numbers = range(100) #0-99 n-1 nd #its memory efficient than list
print(my_numbers)

list_1 = list(my_numbers)
print(list_1)

t1 = tuple(my_numbers)
print(t1)

my_numbers = range(10,100) #10....99 #starting or lower boundary , ending or uypper boundary
my_numbers = range(0,10,3) #0,1,2,3,4,5,6,7,8,9 # steps
print(list(my_numbers))
