#dictornaries are maps - not sequences
#key : value pairs
#key must be an immuntable object
#values can be any data type
#dont use duplicate keys
#keys cannot be null
d = {"firstname": "abuzar khan", "lastname": "mohammed"}
d = {1:"one",2: "two",3: "three",1: "ONE"} # no duplicate keys

d= {
    (0,0): "origin",
    (1,1): "Q1",
    (-1,1): "Q2"
}
d = {"apple": ["phones","airpods","macbooks","smartwatches"], "samsung": ["phones","earpods","notebooks","smartwatches"]}
print(d["apple"][1])


d= {"apple":{"iphones": {"phone1": "iphone15","phone2":"iphone16","phone3": "iphone17"}}}
print(d["apple"]["iphones"]["phone2"])

d = {"firstname": "abdul mateen", "lastname": "mohammed"}
# i want to add  NEW key value pair
d["fullname"] = "moahmmed abdul mateen"
print(d)

del d["fullname"] #del a key value pair
print(d)

#built ins for dictionaries
d = {"firstname": "abdul mateen", "lastname": "moahmmed"}
print(d.keys()) #fetcg on;ly keyys in the list of tuple format
print(d.values()) #fetch only values in list of tuples format
print(d.items())  #fetch key and values in list of tuples format
print(d.get("firstname")) # fetch a value for a particular key

d2 = d.copy() #copy a dict
print(d2)

d.clear() # remove all key value pairs in a dict
print(d)

d = {"firstname": "abdul mateen", "lastname": "moahmmed"}
d.pop("firstname") #remove a specific key value pair
print(d)

d = {"firstname": "abdul mateen", "lastname" : "mohammed"}
d1 = {"footballer":"ronaldo"}
d.update(d1) #add one dictionary to another
print(d)

d.update(d1) #add one dictionary to another
print(d)

d = dict() # {} # contructor
d[1] = "apple"
d[2] = "samsung"
d[3] = "nokia"

print(d)





