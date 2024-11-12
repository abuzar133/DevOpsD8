l = range(0,5)
print(l)

l = [1,2,3,4,5]
for num in l:
    print(num)

#generators are the most easiest way of crearing iterators in memory efficient way
#you can identify generator using yield function
#generators are used to creatw iterators , but with a different approach
#geneartors are simple function which return an iterable set of items, one at a time.
def generate_numbers(n):
    for i range(0,n):
        yield i

l = iter(generate_numbers(6))
for in l :
    print(i)

l = [1,2,3,4,5,6]
sq_l = []
for num in l:
    sq_l.append(num ** 2)

def square_numbers(n):
    for i in range(1,n): #for i in range(1,10)
        yield i ** 2    #i ** 2

for num in square_numbers(10)
    print(num)


#generator expression
#generator expression are similar to list comprerhension , but with parenthesis - ()
squares = (x ** 2 for x in range (0, 10))
for num in squares:
    print(num)

#genertor chaining
# generator chaining is a process of feeding the output of one generator to another generator

numbers = (x for x in range(1,10))
squares = (num ** 2 for num in numbers)
even_squares = (num for num in squares if num % 2 == 0)

 for number in even_squares:
     print(number)