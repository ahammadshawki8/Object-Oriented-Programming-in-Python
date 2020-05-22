# inner class

# we have seen that a class can contain variables and methods.
# but can a class contain another class?
# Interestingly, yes.

# lets see an example:
class Student:
    
    def __init__(self,name,roll):
        self._name=name
        self._roll=roll

        # creating Laptop object inside the outer class
        
        #self.lap=self.Laptop(brand,cpu,ram)
        # we have to use self here as it in the class.
        # we can do this if we pass the attributes when creating a student class.
        
    def show(self):
        print(f"STUDENT INFORMATION \n\t name : {self._name} \n\t roll : {self._roll}")

    # students also have a laptop, so we want a laptop attribute in this class.
    # but the problem is when we talk about laptop,
    # it has different properties and configaration.
    # we can add those properties one by one as an attribute but that isn't great.
    # we can instead create a class and use that.

    class Laptop:
        def __init__(self,brand,cpu,ram):
            self.brand=brand
            self.cpu=cpu
            self.ram=ram

        def show(self):
            print(f"LAPTOP CONFIGURATION \n\t brand : {self.brand} \n\t cpu : {self.cpu} \n\t ram : {self.ram}")
            
            
    # to create the object of the inner laptop class in the outer class, we can do that in the __init__ method.
    # or we can directly create an object of Laptop class outside of the outer class.

s1=Student("Shawki",5130)
s2=Student("Arko",5162)

s1.show()

# creating Laptop object for students. 
s1.lap=s1.Laptop("Lenovo","i5",4)
s2.lap=s2.Laptop("HP","i3",2)
# this object will be an attribute of the student object.

# we can print the attributes of Laptop using,
print(s1.lap.brand)

# we have two different classes with the same name. but we can access both of them.
print()
s1.show()
print()
s1.lap.show()

# NOTE: it is not simmilar to inheritance.
# it can reduce potential name conflicts because it allows for a simmilarly named class to exists in another context.
# another advantage is that it allows for a more advanced form of inheritance
# in which a subclass of the outerclass can override the defination of its inner class.
