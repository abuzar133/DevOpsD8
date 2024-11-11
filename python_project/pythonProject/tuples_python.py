#tuples are immutable
#tuples are hetrogenous sequence

t1 = (1,2,3,4,5)
print(type(t1))
print(t1[0])

t1 = ("abdul","mateen",12,9.5,[1,2,3,4,5])
t2[4].append(100)
print(t2)

print(t2.count("abdul"))
print(t2.index("mateen"))

#tuple concatenation
t1 = (1,2,3,4,5)
t2 = (5,6,7,8,9)
t3 = t1 + t2
print(t3)

#type casting - convertiong one squence to another
l =[1,2,3,4,5]
t = tuple(l)
print(t)