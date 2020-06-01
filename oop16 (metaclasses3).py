# meta classes in python
# part 3
# problem solving with metaclass.

# Problem: inherited docstrings aren't perticularly informative in python.

# here we have two simple class (A and B) and B is the subclass of A
class A:
    def func(self):
        """Doc_String of class A"""
        pass

class B(A):
    pass

# printing the doc string
print(A().func.__doc__)
print(B().func.__doc__) # this is doc string of class B.
# but we are getting doc string of A twice. that is not what we expected.
# so we cant knowthat we are getting the function through class A or B

# More Specificaly,
    # the "nose testing" framework prints out the doc strings of test methods as it runs them.
    # unfortunately, if we have a test suite class that inherits from another class,
    # we wont be able to tell when its running method from parent class vs subclass.


# Solution1:
# the simple solution is that just manually include information in the docstrings.
class A2:
    def func(self):
        """Doc_String of class A2"""
        pass

class B2(A2):
    def func(self):
        """Doc_String of class B2"""

print(A2().func.__doc__)
print(B2().func.__doc__) 

# but there will be lot of work if we have lots of subclasses or methods.
# so there might be a better solution.

# Solution2:
# we can manually change the docstring in the __init__ method.
class A3:
    def __init__(self):
        old_doc=self.func.__doc__
        cls_name=type(self).__name__
        # changing the docstring
        #self.func.__doc__= str(old_doc) + str(cls_name)
        # but we are getting an error because doc string of method object is not writable.
        # NOTE: function docstrings in general are writable but methods docstring aren't.


    def func(self):
        """Doc_String of class """
        pass

class B3(A3):
    pass

print(A3().func.__doc__)
print(B3().func.__doc__) 

# so if there is any way that we can change the doc string before function becomes a method?
# yes. but before that we have to step back.

# what are classes? --> a class is a special kind of object which create other objects called instances.
# type() method tells us the class of an instance. so if we look for the type of a class.
print(type(A3)) # we can see that the type of a class is "type" it means class is a object of type class.

# the type object actually do 3 different things in python.
    # 1. It denotes the type of an object (the types of classes, specifically).
    # 2. It tells us what type an object is.
    # 3. It can create new classes.

# creating class with type
def hello(self):
    return "hello"

class_name="MyClass"
bases=(A3,)
attrs={"hello":hello}

MyClass=type(class_name,bases,attrs)

# Now, lets try to solve our problem again.
# Solution 3:

def make_class(name, bases, attrs):
    for f in attrs:
        attrs[f].__doc__=f"{attrs[f].__doc__} {name}"
    
    cls = type(name,bases,attrs)
    return cls 

def func(self):
    """Doc_String of class"""
    pass

# creating class with make_class
A4=make_class("A4",(object,),{"func":func})
print(A4().func.__doc__) # it prints Doc_String of class A4

B4=make_class("B4",(A4,),{"func":func})
print(B4().func.__doc__) # it prints Doc_String of class A4 B4
# but thats not we wanted. why this happend?

# the answer is that both of these classes A4 and B4 are using same method in the memory.
# so python modified the doctrings of the same object(function) in the memory.
# rather than having two separate function in A4 and B4, they point to the same function.
print(A().func.__doc__ is B().func.__doc__) # it will return True.

# so how can we solve this problem. well we can also create a function on fly using the func_type() class.
# so lets create a function that copy a function.
def copy_function(f):
    func_type=type(f)
    new_func=func_type(
        f.__code__,    # bytecode
        f.__globals__, # global namespace
        f.__name__,    # function name
        f.__defaults__,# default keyword arguements values
        f.__closure__) # closure variables
    new_func.__doc__=f.__doc__
    return new_func

# now lets try again to solve our problem
# Solution 4:
def make_class2(name, bases, attrs):
    for f in attrs:
        new_f = copy_function(attrs[f])
        new_f.__doc__=f"{attrs[f].__doc__} {name}"
        attrs[f] = new_f

    cls = type(name,bases,attrs)
    return cls 

def func2(self):
    """Doc_String of class"""
    pass

A5=make_class2("A5",(object,),{"func":func2})
print(A5().func.__doc__) 

B5=make_class2("B5",(A5,),{"func":func2})
print(B5().func.__doc__)

# hey we solved our problem using metaclass!
# here the make_class function we are using is a meta class.


# python use different complex way to create metaclass.
def make_class3(name, bases, attrs):
    for f in attrs:
        # skipping special methods and non-callable functions since we dont want to mess up with those.
        if f.startswith("__") or not hasattr(attrs[f],"__call__"):
            continue
        
        # copy the function, replace the docstring and return the old method.
        new_f = copy_function(attrs[f])
        new_f.__doc__=f"{attrs[f].__doc__} {name}"
        attrs[f] = new_f

    cls = type(name,bases,attrs)
    return cls 

# and then we are going to create a class with class keyword.
# then we can do this by adding metaclass arguement in the parenthesis.
class A6(metaclass=make_class3):
    def func3(self):
        """doc string of class"""
        pass

class B6(A6, metaclass=make_class3):
    pass


print(A6().func3.__doc__)
print(B6().func3.__doc__)

# note that, here we are not having our expected results for subclass B6.
# it means subclasses not actually rewrite the doc strings correctly.
# this is happening because func3() is not passed as an attribute of B6 (it is already an attribute of A6)
# to make this really work we have to go through all the attributes of all the parent classes and copy them, too.


# so now we know that meta classes are powerful tool. we can use it for many purposes.
# What exactly can we do with meta classes?
# we see that meta classes intervene on class (not instances) creation.
# this gives us the oppurtunity to modify the class's method before the class is created.
# we can,
    # 1. copy each of the functions that will become methods later
    # 2. change doc strings or any other properties of this new functions
    # 3. create the class using these new functions instead of those which are originally given.

# we can find more useful real world example where metaclasses are used.
# for example, django use metaclasses to simplify its interface.
# it gives us opportunity to work with complex classes as user 
# where all the fancy complex parts are handled by the metaclass.

