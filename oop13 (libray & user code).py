# Libray and User code
# suppose we are working in the user code class and we are inheritting form library code.
# we want a specific method that must include in the parant class of the library module.
# in that case we can use assert statements before creation of the User codes class.

# Library Code
class Parent:
    def first(self):
        return "hi"

# User Code
# from module_name import Parent  # actually, library and user code situated in two different module.
assert(hasattr(Parent, "first")),"Must need to have first() function"
class Child(Parent):
    def second(self):
        return self.first()


# now lets say, we are working with the library code and dont change the user code.
# but we want some functions defined in the user code's class so that our library code doesn't crash.
# we can do that in 3 technics.
    # 1. __build_class__ method
    # 2. meta class
    # 3. __init_subclass__ method


# __build_class__ method
# this method allows us to hook into and do cool things in the process of building classes.

# this method is from builtins module
import builtins

# first grab the old __build_class__ within our interpreter.
old_method = __build_class__

# now lets create our own method.
def new_method(*args,**kwargs): 
    # NOTE :
        # here **kwargs are those arguements that we pass in the perenthesis after the class name.
        # it is not the attributes and methods in the class body.
    print(f"Building class with arguements:{args} and key-word arguements: {kwargs}")
    return old_method(*args,**kwargs)

# now replace the old method with our new one.
builtins.__build_class__=new_method

# Now if we create a class we can see the magic is happening.
class Boss():
    pass
# we can see that the class is building.
# Building class with arguements:(<function Boss at 0x000001C4057B1AF0>, 'Boss') and key-word arguements: {}


# now we can do some cool stuffs with this.
# first create a class.
class InfrastructureLibary:
    def primary(self):
        return self.secondary()


class User(InfrastructureLibary):
    def secondary(self):
        return "secondary"

# suppose we are working with the low-level programming team when we are developing the first class.
# we have no right to change the User class.
# we can see the the User class must need to have the secondary() method unless our code will fail.
# so how to remind the developer of the User class that they must need to include secondary() in there code.
# well we can use the __build_class__ method here.

import builtins

old_method2 = __build_class__

# here we have changed the *args little bit. 
# it is actually separated into the name of the functions, name of the class and its base class.

def new_method2(function,name,base=None,**kwargs):
    if base is InfrastructureLibary:
        print("WARNING: You must need to create a secondary() function.")
    if base is not None:
        return old_method2(function,name,base,**kwargs)
    return old_method2(function,name,**kwargs)

builtins.__build_class__=new_method2

# now if we create a child class of the InfrastructureLibary class, then we can see that gives us the warning.
class NewUser(InfrastructureLibary):
    def secondary(self):
        return "secondary"

# but in the Real world example, developers wont solve the problem like this.
# rather than they use MetaClass. see metaclass.py module for better understanding.
        
class Meta(type):
    def __new__(self,class_name,base,attrs):
        if not "secondary" in attrs:
            print("WARNING: You must need to create a secondary() function.")
        return super().__new__(self,class_name,base,attrs)

class InfrastructureLibrary2():
    def primary(self):
        return self.secondary()

class User2(InfrastructureLibrary2,metaclass=Meta):
    def secondary(self):
        pass

# But MetaClass is pretty complex topic in python.
# so the developers of python have created a new method called __init_subclass__
# it allows us to hook into the subclass of any parent class.
# __init_subclass__ runs after the creation of the subclass.

class Infra:
    def __init_subclass__(cls,*args,**kwargs): 
        super().__init_subclass__(*args,**kwargs)
        print("Must Have to include last() method")
        print("Creating subclass, name :", cls.__name__)
    
    def first(self):
        return self.last()

class UserCode(Infra):
    def last(self):
        return "last"

# __init_subclass__ has more things to learn. i will learn them when I need them.

