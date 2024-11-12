#polymorphism is an ability (in OOP) to use a common interface for multiple forms(data types)

class Animal:
    def speak(self):
        print("Every Animal speaks")

class Dog(Animal):
    def speak(self):
        print("dog barks")

class cat(Animal):
    def speak(self):
        print("cat meows")


dog_1 = dog()
dog_1.speak()  #method overriding

cat_1 = cat()
cat_1.speak() #method overriding

#DUCK TYPING
#duck typing is a concept related tp dynamic typing where the type or the class of an object is less importantt than the method
#defination : if you look like a duck quack like a duck you are a duck

class Circle:
    def draw(self):  #method with the same name in all the classes
        print("Drawinmg circle")

class Triangle:
    def draw(self):    #method with the same name in all the classes
        print("Drawing triangle")

class Square:
    def draw(self):     #method with the same name in all the classes
        print("Drawing square")

circle1 = Circle()
triangle1 = Triangle()
square = Square()

def draw_shape(shape): # Duck typing : the draw method is not defined in the function,but it will work for any object that has draw
    shape.draw()

draw_shape(circle1)
draw_shape(square1)
draw_shape(triangle1)