# meta classes in python
# part 2

# here we will create our own metaclass which will inherit from the type class.
# this is pretty simmilar thing as the default type metaclass.
# but we will change how the object is constructed so that we understand what can we actually do with metaclass.
# so lets get started

# creating meta class
class Meta(type): 
    # we not necessarily have to inherit form type. but in our purpose that will work.
    # the reason for that is type does some other operations when creating a class.
    # if we dont inherit from type, our class wont be a metaclass, 
    # it will be general class which use type metaclass to create a class.
    # besides, this inheritances will give us the ability of overriding methods of type class

    # now we will define a __new__ method. it executes before the __init__ method.
    # so this is always called first when a object is created.
    def __new__(cls, class_name, bases, attrs): 
        # remember that, in type arguement we pass name, class_name, bases and the attributes.
        # NOTE: it is not a class method but by convention we pass cls instead of self as we are creating class object.
        
        # do some more stuffs to override this __name__function:
        print(f"Creating Class with {attrs}")
        
        # creating class in return 
        return type(class_name, bases, attrs) 
        # here we can use super().__new__ method instead of type as type is the parent class.
        # return super().__new__(cls,class_name,bases,attrs)
    # __init__ method changes the values and takes the parameters in.

# now we will create another class
class Dog(metaclass=Meta): # defining the new Metaclass in parenthesis.
    # creating some attribute
    x=5
    y=8
    def func(self):
        return "hello"
# now we can see that it prints our message which we defined in the __new__ method.

# now we know the information, metaclass can be extreamly powerful.
# we can hook into the construction of a class and we can modify the construction.
# lets change all of the attributes we have here into upper case.

class NewMeta(type): 
  
    def __new__(cls, class_name, bases, attrs): 
        
        new_attrs={}
        for key,value in attrs.items():
            if not key.startswith("__"):
                new_attrs[key.upper()]=value
            else:
                new_attrs[key]=value

        print(f"Creating Class with {new_attrs}")
        
        return type(class_name, bases, new_attrs)
  
class Cat(metaclass=NewMeta):
    x=5
    y=8
    def func(self):
        return "hello"

# now lets create an attribute of Cat
c=Cat()
# now lets print out the x attribute of c object.
#print(c.x)
# this will give us an error. but we have defined x attribute in the Cat class.
# well we are getting error because we changed the x attribute to X in the metaclass.
print(c.X)
# same goes for the func() method.
print(c.FUNC())


# now we have undertand metaclass, now we can do whatever we want when working with class.
# we can change the bases, class name, attributes, do certain operations based on the parametes.

# metaclasses are great for doing complicated things """ inside of the frameworks """. NOTE
# metaclass is nice when we are writting library code and we want user code to be very specific.
# when user codes classes are inheritting form a specific class situated in the library code,
# we can force them or tell them to initialize certain methods in that class so that our code doesn't crash.
# actually, in every example of metaclass we will see that,
# there is a parent class and some subclasses 
# and we want to control the behaviours of subclasses without explicitely writing code in them. 

# again there are more complex topics in metaclass. we can see them in the python documentaion.
# we dont need to use them much. we should use them when we are 101% sure about what we are doing.
# they will make our code really hard to understand.
# but understanding these types of expert topics in python will really help us to code better,
# because then we can become sure what is going on the background.
