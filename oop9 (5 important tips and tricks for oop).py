# Tip 1
# multiple inheritance
class A:
    def intro(self):
        print(" I am from class A")

class B:
    def intro(self):
        print(" I am from class B")

# we can create a subclass and inherit from multiple parentclass too.
class C(A,B):
    pass

# now if we create a object of C class and apply the intro function to it.
object_C=C()
object_C.intro()

# we can see that it is executing the class A intro() function.
# python always follow a order for execution of differnt functions.
# we can see the order by mro() function.
print(C.mro())

# we can see that the order is 
#[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
# so it first search C, then A, then B and after that object.

# what is MRO?
# Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes.
# Especially it plays vital role in the context of multiple inheritance as single method may be found in multiple super classes.

# super() method
# we have already seen a use case of super() method. we have use this to inherit the constructor from the parent class.
# actually, super() is used in the subclass for calling a function which is situated in the parent class.
class G:
    def num(self):
        print(1)
class H(G):
    def num(self):
        print(0) 
        super().num()# this num() is situated in the parent class.

object_H=H()
object_H.num()

# tip 3
# operator oveloading
# we see how differnt operators work in python. they are nothing but dunder methods.
# we can actually change the characteristics in python.
# it is called operator overloading.
class Myoperats:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return (self.value **2) + (other.value**2)

num1=Myoperats(5)
num2=Myoperats(12)
print(num1+num2)
# here we have change what our + operator actually does.

# tip 4
# object life cycle
# object have three periods in their life in the memory.
# they are Creation, Manipulation and Destruction.

# when we create a object by a class, __new__ and __init__ method start working.
# and other part of the code can use the object and manipulate it.
# we can destroy the object after we used it. this is called "garbage collection".
# when "garbage collection" is  done the memory that the object used become free and we can use it for another reason.
# python automatically done the "garbage collection" after we use the object.

# so we can now make an ideal defination of "garbage collection"
# The process by which Python periodically frees and reclaims blocks of memory 
# that no longer are in use is called Garbage Collection.
# python's garbage collector runs during program execution and is triggered 
# when an object's reference count reaches zero.

# what is reference count?
# when we code, an onject can be linked with multiple objects.
# the number of objects that an object is linked is called its reference count.
# lets see an example.
a=42 # a is linked to 42. so its reference count is 1
b=a  # a is linked to b. so its reference count is 2
c=[1,2,3]
c[0]=a # a is linked to c. so its reference count is 3

# now we can manually decrase the reference count by del method.
del a # a is not linked to 42. so its reference count is 2
b=98 # a is not linked to b. so its reference count is 1
c[0]=54 # a is not linked to c. so its reference count is 0

# when a reference count become 0. it no longer any use for us. So, python delete the object a from the memory. 
# that is what "garbage collection is"

# tip 5
# data hiding

# oop has 4 important concepts
# they are encapsulation, inheritance, polymorphism, and abstraction.

# encapsulation means a technic where we combine some variables and functions and express them as a single unit.
# this concepts makes a barrier between the variables of different classes.
# we can only grab the variables by excuting some functions of the same class.
# this is called "data hiding".
# in other words, data hiding means hiding the implimentation details of a class.

# in other programming language, we can use keywords(access modifiers) to make class attribute and methods private or protected.
# but in python, things are little different. they said, we are all consenting adults here.
# it means it is not advisable to keep any class's element protected from outside's access.
# so python dont have any real method for data hiding.
# instead of that, python advise not to access important implementation details from outside.

# weakly private
# when we use underscore(_) before an attribute or methods name, we are saying that they are weakly private.
# we can use them outside of our class but we should not access them outside of our class.
class Mlist:
    def __init__(self,*contents):
        self._hidden=[*contents]
    def add(self,*contentsr):
        self._hidden.extend([*contentsr])
    def _show(self):
        print(self._hidden)

l1=Mlist(1,2,3,4,5,6)
l1.add(7,8,9)
l1._show()

# note that: if we import a module having weakly private attributes and methods, then they are not imported.
# even if we use from module_name import * 
# so they remain private.

# strongly private
# when we use double underscore(_-) before an attribute or methods name, we are saying that they are strongly private.
# python change their name little bit. so we cant access them from the outside.

# mainly, it doesn't done for resisting the access.
# it is done for if we have any other attribute in the subclass with the same name, so that it wont confilct with that.
class Make:
    __cake=10
    def print_num(self):
        print(self.__cake)

a=Make()
a.print_num()
# print(a.__cake)
# we cant run this line. it would say that, Make has no attribute __cake.
# but we can still access the attribute like this. _classname__attributename
print(a._Make__cake)
# actually, python make the change to its name.
 