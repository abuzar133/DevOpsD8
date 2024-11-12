#Encapsulation is the process of restricting access to methods and variables
#encapsulation is achieved by using access specifiers such as private,protected,and public
#in python we can acheive encapsulation using the following access specifiers:
#public: accesiblr from anywhere, default access specifier in python
#protected : accesible within the class and its subclasses
#private: accessible only within class

class Person:
    def __init__(self,name):
        self.name = name #public variable
        self._age = 29 #protected variable #single underscore
        self._ssn = "873-51-2784" #protected variable #single underscore
        self.__salary = 10000 #private variable #doubl;e underscore

    def display(self):
        print(self.name)
        print(self._age)
        print(self._ssn)
        print(self.__salary)

    def _get_age(self):
        return self._age

    def __get_ssn(self):
        return self._ssn

    print(locals())

person1 = Person("Jhon")
print(person1.name)
print(person1._age) #can still access protected variable
person1._age =45
print(person1._age)
print(person1._Person__salary) #private variable can be accessed by using class _ example this is called name mangling or DUNDER
                                   