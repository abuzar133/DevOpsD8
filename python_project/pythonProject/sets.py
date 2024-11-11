#sets are un orderes collection of unique elements
#sets are mutable
#sets can only store immutable objects
s = {1,2,3,4,}
print(type(s))
print(s)

#built ins
s.add(100)
print(s)
s.remove(100)
print(s)

s1 = {1,2,3,8}
s2 = {4,5,6,8}

#set union
print(s1.union(s2))
print(s1 | s2)

#set intersection
print(s1.intersection(s2))
print(s1 & s2)

#booleans
a = True
b = False

s = set()
s.add(1)
s.add(2)
s.add(3)
print(s)

#interview question
l= [1,1,1,1,2,2,2,23,3,3,3,4,4,4,5,5,5,6,6,7]
s = set(l)
print(lists(s))
