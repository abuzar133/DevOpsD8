#inheritance is a way of creating a new class usingdetails of an existing class withoutmodifying it
#the newly formed class is derived class( oe child class).
#similarly , the existing class is a base class(or parent class)

class animal: #super class, parent class,base class
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def get_details(self):
        print(f"name:{self.name}, colour: {self.colour})

    def speak(self):
        print("animal speaks")

class Dog(animal): #subclsss, child class, derived class
    def __init__(self, name, colour, breed): #constructor with parent class attributes and child class attributes
        super().__init__(name , colour) #calling the constructor of the parent class
        self.breed = breed

    def dog(self):
        print("dog barks")

dog1 = Dog("tommy" ,"brown","labrador")