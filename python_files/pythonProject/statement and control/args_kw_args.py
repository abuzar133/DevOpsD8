#interview question
#
def sum_of_nums(*args): #*args is an arbitary num of arguments, it will be in tuple format
    for num in args: #(10,20,30...)
        print(num)
        return sum(args)

l = sum_of_nums(1,2,3)
m = sum_of_nums(10,20,30,40,50,60)
n= sum_of_nums( 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8)
print(l,m,n)


def func(a,b,*args , c)  # a , b are positional parameters *args is arbitary star parameter and c is positional parameter
    print(a)
    print(b)
    print(args)
    print(c)

func(1,2,4,5,6,7,8,9,10, c = 100) #a ,b positional parameters , *args arbitary star parameter c is positional paramterr

#(*args comes in a tuple format )
# **kwargs are in dictionary format


def func(**kwargs): #{"a" : 1,"b" :2 , "c" : 3}
    for k , v in kwargs:
        print(k,v)

func(a=1 ,b=2 ,c=3)

def func(a,b,*args, **kwargs): # this should be the sequence cant be first kwargs and then args
    print(a)
    print(b)
    print(args)
    print(kwargs)

func(1,2,3,4,5,6,7,8,9,10,11, x = 100 , y =200, z = 300)


