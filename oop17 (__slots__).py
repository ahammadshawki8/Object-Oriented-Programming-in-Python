# __slots__ dunder method in python

# here we will demonstrate in code why using __slots__ results faster instant attributes access.
# and space in memory become more and more relevent as the number of instant creation grows.

# first lets create two classes identical in may ways.
class Planet:
    def __init__(self,cities):
        self.cities = cities

# creating object
earth = Planet(["Dhaka","DC"])

class SlottedPlanet:
    # the only difference between this two class it that it has a __slot__ apecial attribute at the top.
    __slots__ = ["cities"] # it takes strings and this strings are the name of all attributes
    def __init__(self,cities):
        self.cities=cities

# creating object    
slotted_earth = SlottedPlanet(["Madrid","Paris"])

# lets print those objects.
print(earth)
print(slotted_earth)

# printing the attributes of those objects.
print(earth.cities)
print(slotted_earth.cities)

# we can see that there is no difference.

# now lets add a new attribute in the earth object called country.
earth.country=["Bangladesh","United States"]
# if we try to do the same with the slotted_earth we get an attribute error.
#slotted_earth.country=["Spain","France"]
# the only attributes that this object can have are those which we have provided to the __slots__.

# so we can even left the __slots__ attribute empty.
class EmptyBin:
    __slots__=[]
# creating object
empty_object=EmptyBin()
# we cant create any attribute of that object.
#empty_object.att="new attribute"


# why cant we add attributes in a slotted object in the general way?
# we can also store attributes in a general earth object by storing them in the instant dictionary.
# we can access the dictionary by __dict__ method.
print(earth.__dict__)
# but in the slotted_earth we do not have any __dict__ method.
#print(slotted_earth.__dict__)
# this will give us an attribute error.
# so SlottedPlanet class dont even created a dictionary.

# we know that dictionary even though empty one take up space.
# so since slotted object dont create dictionary we can have a much space in the memory. so it is a lightweight object.
 
# we can see the space of any object by the getsizeof() method from the sys module.
import sys
# we can see that this object take 48 bytes space.
print(sys.getsizeof(earth))
# and its dictionay take 104 bytes space.
print(sys.getsizeof(earth.__dict__))
# so in total 152 bytes of memory usage.

# again the slotted_earth also takes only 48 bytes space.
print(sys.getsizeof(slotted_earth))
# so we can see that the memory space is decrreased though a little portion of it.
# but if we have big data, then it will be a great benefit by releasing much GBs of memory
# and it also can give us a performance boost.


# lets see the time it needed to perform operations in a regualar object vs slotted object.
# we have to import timeit module for that.
import timeit

# creating two classes
class UnSlotted:
    pass

class Slotted:
    __slots__=["values"]

# creating a get_set_delete_func function
def get_set_delete_func(obj):
    # creating another function which will
    def get_set_del():
        obj.values=[0,1]   # set values
        obj.values         # get values
        del [obj.values]   # delete values
    return get_set_del     # returnning the inner function

# creating object
non_slotted_obj = UnSlotted()
slotted_obj=Slotted()

# repeating operations multiple time using repeat() function of timeit module 
# and printing the minimum process time (in seconds) using min function(). 
print(min(timeit.repeat(get_set_delete_func(non_slotted_obj),repeat=5)))

# doing the same operation with slotted_obj.
# we can see 15% to 20% improvement in time.
print(min(timeit.repeat(get_set_delete_func(slotted_obj),repeat=5)))

# we can not only use classes having __slots__ attributes for memory and time boost,
# we can also use them in the library code 
# and ensure that the user cant define new attributes and methodsin our class
# which can make our class unstable.
# library code
class Library:
    __slots__=["attr1","attr2"]
    def __init__(self,attr1,attr2):
        self.attr1=attr1
        self.attr2=attr2

# user code
user1=Library(0,1)
# we cant create more attribute here.

# now lets see inheritance of slotted class.
class Computer:
    __slots__=["ram"]

slotted_comp=Computer()
slotted_comp.ram="4 GB"

# create a subclass of the slotted class
class Laptop(Computer):
    pass

inherited_laptop=Laptop()
# if our subclass dont initiatize __slots__ attribute,
# then every object of our subclass will still have instant dictionary.
print(inherited_laptop.__dict__)

# printing the size of inherited object
print(sys.getsizeof(inherited_laptop))
print(sys.getsizeof(inherited_laptop.__dict__))

# adding attributes to inheritted object.
inherited_laptop.ram="8 GB"
inherited_laptop.rom="2 TB"
# printing the instant dictionary again.
print(inherited_laptop.__dict__)
# we can see there is newly created rom attribute but no previous ram attribute.
# actually the parant class will continue to be sloted if we created object of a subclass.
# the attribute thst was presious defined in the __slots__ of parent class will store there.
# whereas the newly defined attributes will store in the instant dictionary of that object. 

# lets do that again. but in this time we will use __slots__ attribute in the subclass and set that equal to empty.
class Desktop(Computer):
    __slots__=[]

inherited_desktop=Desktop()

inherited_desktop.ram="16 GB"
# though the __slots__ is empty, we can store the ram attribute which was previously mentioned in the __slots__ attribute of parent class.
# but we cant add another attribute here it will give us an attribute error.
#inherited_desktop.cpu="i7"
# again, we cant see the __dict__ attribute too as it doesn't have one.
#print(inherited_desktop.__dict__)

# what if we want to add attributes to class dynamicaly?
# then we can add "__dict__" attribute in the __slots__ attribute.
class Dynamic:
    __slots__=("x","__dict__") # we can use both list or tuple to our __slots__ method. but we should use tuple if we want to make it immutable.

dynamic_slotted=Dynamic()
dynamic_slotted.x=1
dynamic_slotted.y=2
dynamic_slotted.z=3
dynamic_slotted.p=4
# it has a __dict__ method as we mention it earliar in the __slots__
print(dynamic_slotted.__dict__)
# we can see that the first attribute x not in the __dict__ as we add that separately in the __slots__
# but "y", "z", "p" attribute are in the __dict__

# NOTE: one thing we have to be very careful about that we should not add same attribute in the parent and subclass's __slots__ attribute.
class Parent:
    __slots__=("x")

class Child:
    __slots__=("x","y") # x is in the both __slots__ method.

class NewChild:
    __slots__=("y",)

# creating object
child_slotted=Child()
new_child_slotted=NewChild()
# printing the size of the object.
print(sys.getsizeof(child_slotted))
print(sys.getsizeof(new_child_slotted))

# this wont give us any error. 
# but doing this will force our object to take op more space than they need to.
# we can see that it takes more bytes than necessary.

# NOTE: in a very large codebase, it is important not to use __slots__ unless very much necessary.
# because there can be problem in multiple inheritance.
class ParentA:
    __slots__=("x",)
class ParentB:
    __slots__=("y",)

# our Subclass inherits both from ParentA and ParentB
class Subclass(ParentA,ParentB):
    pass
# when both parents have a non-empty __slots__, 
# then we will have an TypeError saying "TypeError: multiple bases have instance lay-out conflict"

# to overcome the problem one of the parent has to have a __slots__ defined with an empty list or tuple.
