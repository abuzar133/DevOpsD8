#exception handling - try except finally blocks
#it basiclly handles the error that occurs during the execution of the program.
#except block all executed when an error occurs in the try block .
l ={"a":5, "b":10, "c":15}
try:
    print(l["d"])#keyerror exception
    print("this is inside try block")
except Exception as e :
    l["d"] = 20
    print("this is inside except block")
print(l)

a = 2
b = 0
try:
    print(a/b) # zero divisoon undefined
except Exception as e:
    b = 2
    print(a/b)

l = ["a", "b", "c", "d","e","f", 5]
try:
    for char in l:
        print(char + "ppp") #type error when char is 5
except Exception as e:
    print(f"for the char{char},concatenation with str is not possible")
    print(str(char) + "ppp")


#finally block
#finally block are always executed irresepective of exeception occurs or not .
l = [1,2,3,4,5,6]
try:
    print(l[2]) #index error
except Exception as e:
    l.append(7)
    l.append(8)
    print(l)
finally:
    print("this is finally block")

#mutiple exception blocks
l= [1,2,3,4,5,6]
try:
    print(l[1]) #index error
    print(l["a"]) # type error
except IndexError as e:
    print("Indexerror occured")
except TypeError as e:
    print("typeerror occured")

