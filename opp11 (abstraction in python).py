# abstraction in python
# it is one of the main principles in oop

# DEFINITION:
# abstraction is the act of removing elements of specificity to emphasize commonality.
# it is the process of describing things using only the important details for the task at hand.
# in computer context, this involvs only providing attributes and methods to an object
# that are useful for that perticular task only.


# Abstract Class
# abstract classes are the classes that contains abstract methods.
# an abstract method is a method that is declared, but contains no implementation.
# abstract classes cannot be instantiated it means we cannot create objects of the abstract class. 
# and requires subclasses to provide implementations for the abstract methods (we can create objects of subclass)
# Subclasses of an abstract class in python are not required to implement abstract methods of the parent class.

# we want to make an abstract class.
# in python there is a pre-defined abstract class called ABC(abstract base class).
# we have to import ABC class from abc module.
from abc import ABC, abstractmethod

# here A is an abstract class
class Configure(ABC):
    # lets create an abstract method. we have to use the @abstractmethod decorator.
    # we have to import it from abc module
    @abstractmethod
    def display(self):
        pass
    # so abstract method has declaration but no implementation.

# if we want to implement this abstract method we need to create a subclass.
class Mechanic(Configure):
    # implementing the abstract method by overriding
    def display(self):
        print("this is display method for mechnic")
        # we can call the abstract method from parent class by super() method.
        super().display()
        # generally we dont have any implementation in abstract methods. but if we have any then we can use that.


# we have to create object of the child class.
m=Mechanic()
m.display()



# what if we have two different abstract methods in the parent calss and only one overridden abstract method in the child class?

class Configure2(ABC):
    @abstractmethod
    def engine(self):
        pass

    @abstractmethod
    def color(self):
        pass 

class Mechanic2(Configure2):
    def engine(self):
        print("this is engine method for mechnic")

    # def color(self):
    #     pass

# here we have two abstract methods in parent class
# and we only have implemented one of the methods in the subclass.
# now can we create an object for the subclass?
# m2=Mechanic2()
# m2.engine()
# we can see that we cant do it because there is another abstract method remaining 
# which our subclass inherit from the parent class and we havent implement that.
# so our Mechanic2() class is also a abstract class

# how to solve this problem?
# there is several ways we can do this.
# method 1: we can implement the remaining function in the subclass.
# method 2: create another subclass of the subclass Mechanic2() and implement the remaining function there.

class Sub_Mechanic2(Mechanic2):
    def color(self):
        print("this is abstract color method form a subclass of mechanic2")
        super().color()

# create the object of the Sub_Mechanic2() class.
m3=Sub_Mechanic2()
m3.engine()
m3.color()



# we can also create a constructor in the abstract class.
class Cal(ABC):
    def __init__(self,value):
        self.value=value
        # NOTE: here value is a local variable for the __init__ constructure.
        # when we use self.value it becomes class variable for the entire class.

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass

class C(Cal):
    def __init__(self,value):
        super().__init__(value)

    def add(self):
        return self.value+100
    def sub(self):
        return self.value-10

obj=C(100)
print(obj.add())
print(obj.sub())

# Why should we use abstract class?
# we should use abstraction when we are designing an application in a oop way.
# if we create an abstract class, the subclasses will have some restrictions to which method they musst have to defined.
# for example, in the previous example our Mechanic2 class must have 2 methods which are color() and engine()
