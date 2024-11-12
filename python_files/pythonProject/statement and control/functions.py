# functions  - are most logical and smaller block of codes that can be used respectively
# to execute the function's code , you need to invoke / call the function
# its denoted by () parenthesis
#def is keyword used for funtions

def print_data():
    print("hello world")
    print("how are you all")
    print("It is a fine morning")

def add_two_num():
    a = 5
    b = 10
    print(a+b)

#add_two_num()

def add_two_num(a,b) : #functions with parameteers
    c =  a + b
    print(c)

add_two_num(5,10) #these are cslled arguments
add_two_num(10,25)
add_two_num(55,100)
add_two_num(1000,100000)

def add_more_num(a , b, c):
    d = a + b + c
    print(d)
add_more_num(1,2,3)


# retrun keyword
def add_more_num(a, b, c): #functios with paramteres
    return a + b + c
sum_of_nums = add_more_num(100,10,1)
print(sum_of_nums)




def calculate_sq_list(list_nums):#[1,2,3,4] [1,4,9,16]
    sq_list = []
    for num in list_nums:
        sq_list.append(num ** 2)
    return sq_list #[1,4,9,16] #return in list value
def calculate_add_2(sq_list): #[1,4,9,16]
    added_list = []
    for num in sq_list:
        added_list.append(num + 2)
    print(added_list) #[3,6,11,18]

list_squared = calculate_sq_list([1,2,3,4]) #[1,4,9,16]
calculate_add_2(list_squared) #passed returned value to another function

def sum_of_nums(*args): #*args is an arbitary num of arguments, it will be in tuple format
    for num in args: #(10,20,30...)
        print(num)
        return sum(args)

l = sum_of_nums(1,2,3)
m = sum_of_nums(10,20,30,40,50,60)
n= sum_of_nums( 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8)
print(l,m,n)


