# meta classes in python
# part 1

# in this module we will cover meta classes.
# meta classes is a fairly complicated but interesting topic in python.

# we are going to start from how classes are created, instantiated, the way they work in the lower level of python.
# and then we will learn what metaclasses are, how they actually work and how would we want to use them.
# here we will learn the basics of metaclass.
# if we really want to use these we need to look to the python documentation for beyond the basics.

# why metaclass?
# there are several things we cannot do with classes.
# meta class allow us to do those things.

# lets get started.
# lets we create a class inside a function.
def hello():
    class Hi:
        pass
    
    return Hi
# here we wont getting any error.
# it is legal in python to create a class inside a function and return it.
# the reason we can do that in python is that in python classes are objects.
# infact, "EVERYTHING IN PYTHON IS AN OBJECT" NOTE that

# what it mean to be an object?
# it means they are kind of living things.
# we can interact them within runtime, we can pass in parameters, we can store it, save it, modify it etc.

# we might say how can be classes are objects?
# we thought that classses create object for us.
# its true. but it doesn't mean that class doesn't an object.

# so if class is a object, then we might have any higher level class which created that class for us.
# that is a meta class

# What does meta class actually do?
# a class defines the basic rules for the objects. it defines the attributes, parameters, methods etc.
# whereas a meta class defines the rules for a class.

# so if we create a class we need the metaclass to create it.
# this happens automatically in python.

# now lets create another class.
class Test:
    pass

# lets print an object of that class
a = Test()
print(a)
# we can see that it is saying <__main__.Test object at 0x000001FA3B071C70>

# now lets print the class.
print(Test)
# we can see that it is saying <class '__main__.Test'>
# we can see that it doesn't tells us that it is an object. but it is an object.

def func():
    pass
# we can use the type method to see the type of any object.
print(type(func))
print(type(3))
print(type("h"))
print(type(a)) # here we are getting the type <class '__main__.Test'>
# lets see the type of the class as it is a object too.
print(type(Test)) 
# we can see that it is printing <class 'type'>
# it is pretty awkward. we can see that the type of the class is "type"
# here type is the metaclass. it defines the rules and create the class for us.

# we can use type to create a class manually. 
MyTest=type("MyTest",(),{})
# this is completely equivalent to the first time when we created the Test class.

# we can create a object of that class also.
b=MyTest()
print(b) # we can see that it is giving <__main__.MyTest object at 0x000001F599A71DC0>

# we can also print the class
print(MyTest)
# we can see that this is giving us <class '__main__.MyTest'>

# it is probably the less used technic for creating a class in python.
# so we can create a class using metaclass "type" 
# and we need to pass the name of the class, 
# the name of the base class in () 
# and the name of the methods and attributes in {}

# so lets see an example of a class using methods and attributes.

# doing some pre work-
class Parent:
    def show(self):
        print("hi")

def func2(self): # since we will add this function to the class, we need to use self
    return "Hello"

# defining the class with all options using type class.
NewTest=type("NewTest",(Parent,),{"x":5,"new_func":func2})
# note that here we have use comma(,) after the parent class as we want to ensure that as tuple.

# creating a object of that class.
t=NewTest()

# using the attributes and methods of t object.
print(t.x)
print(t.new_func())
print(t.show())

# we can also create attributes outside of the class just like the regular class.
t.y=4
print(t.y)

# So this is how we use type and use metaclass, create class with the metaclass. 
# so we have seen that, metaclass is any callable that takes parameters for:
    # 1. the class's name
    # 2. the class's bases (parent class)
    # 3. the class's attributes (variables and methods)
# the type is the default metaclass in python.

# so this is the basics now we will actually dive into the real usecase of meta classes.
# we will see how to create custom metaclass with the help of default type metaclass.
"""go to oop15(metaclasses2).py"""