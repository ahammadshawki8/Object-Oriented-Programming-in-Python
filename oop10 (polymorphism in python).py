# polymorphism
# it is one of the main principle of oop programming.

# sometimes a object comes in many types and forms.
# so we can create a method, that will access all types of that object 
# and do the same thing regardless what type of the object it is.
# the idea is called polymorphism.
# it means there will be one function but it can behave various ways depending on the type of the input.

# polymorphism can be achieved by overriding and overloading in python.

# method overriding:
# it means having two method with the same name but doing different tasks.
# it means one of the methods override the other.
# if there is any method in the parent class and a method with the same name in the child class,
# then if we execute the method, the method of the corresponding class will be executed.
class Parent:
    name="Father"
    def num(self):
        print(1)

class Child(Parent):
    # overriding variable
    name="Son"

    # overriding num() method in the child class
    def num(self):
        print(0) 

object_P=Parent()
print(object_P.name)
object_P.num()

object_H=Child()
print(object_H.name)
object_H.num()

# here we are using the same method and variable for 2 different class 
# and they are handling each class separately which is polymorphism


# overloading
# in python we can define a method in such a way that there are multiple ways to call it.
# if we are given a single method or function, we can specify the number of parameters our self.
class Human:
    def hello(self,country=None):
        if country is None:
            print("Hello")
        elif country=="ENGLAND":
            print("Hello!")
        elif country=="GERMANY":
            print("Gutan Tag!")
        elif country=="FRANCE":
            print("Bonjour!")
        elif country=="MEXICO":
            print("Ola Amigo!")
        elif country=="INDIA":
            print("Namaste!")
        else:
            print("Hey!")

obj=Human()
obj.hello("MEXICO")
 
obj_2=Human()
obj_2.hello("FRANCE")

# here hello is the same method but it will work differently depending on the arguements.
# we can do polymorphism with this overloading too.


# there is another type of overloading which is operator overloading.

# add(+) operator is the same operator but works differently for different types of input.
# it sum the value of int and float objects
# and it concate string objects
# it extend list objects.

# we can also create our own class and change the functionality of the add(+) operator.
class Special():
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return self.value * other.value
        # changing the behaviour of + method (making it *)

num_1=Special(100)
num_2=Special(20)

print(num_1+num_2)
print(67+89)
print("Good "+"Boy")
# here + is the same operator but it returns different values for different types of objects.
# so it is a example of operator overloading.
