# oop1(object oriented programming)

# there are 3 styles in programming.
# 1. Imperative : doing programming with diffferent loops, if/else statement and general basics.
# 2. Functional : doing programming with pure, higher order, recursive and all types of functions.
# 3. Object oriented: doing programming with classes and objects.

# OUTSIDE OF THE TOPIC:
# pure function is the type of function which didnt effect any out code of the function. exp: adding calculater
# impure function is the type of function which effect any out code of the function. exp:appending to a list
# higher order function is the type of function which either take a function as an arguement or return
# a function as their return value is called a higher order function. exp:map,filter


# classes and objects

# what is an object?
# an object is basically a collection of properties which can be expressed as variables and some functions.
# we need to put the object in a variable.
# that variable will contain whole set of properties of the object.
# object contains data which are unique to each other.

# what is attributes?
# the variables within the object are called either "Instance variables" or "attributes".

# what is method?
# the functions within the object are called methods.

# what is a class?
# a class is basically like a blue print from which we can make objects.
# a class doesn't refer to any perticular object.
# we need to give a suitable name to a class.
# the first letter of the name must be "capitalize".

# creating a class.
class Employee:
    pass
# here we write the pass method because we are not going to work with it right now.

# creating a object.
emp1 = Employee() # this simply says create a new object with the class "Employee".
# here we are using default python constructer for this class "Employee".

# setting attributes or instances(variables) to an object.
emp1.first="ahammad"
emp1.last="shawki"          
emp1.pay=1000
# here each arrtibutes are unique to other.

# we can now create a new object in this class too
emp2=Employee()
emp2.first="christiano"
emp2.last="ronaldo"
emp2.pay=2000

# printing from class
print(emp1.pay) 
print(emp2.pay)

# but in this code, we are writing same line in the object again and again.
# that's OK but not great!!
# it is too messy.
# it can give us an attribute error if we mis-spell any attibute incorrectly in the object.
# so, the best way to deal with it is using a constructer.

# lets create the same class using constructer.
class Employee1:
    def __init__(self,first,last,pay):# this is called a constructer.in python to make constructer we must use the keyword "__init__"
        self.first=first
        self.last=last      # in our constructor we are setting the instance variables or attributes.
        self.pay=pay
        self.email=first +"."+last+"@company.com"

# when we create methods within a class,they receive the attributes as the first arguement automatically.
# and by convention we should call the attribute "self".
# we can call it whatever we want. But it is a good idea to stick with the conventions.
# so, we need to write "self" as the first arguement of the constructer.
# once we have a constructer in our class the default constructer will stop working.

# now we can pass value in our constructor(outside the class)
emp3=Employee1("zinedin","zidan",3000)
emp4=Employee1("sergio","ramos",4000)
# in our object, attributes pass automatically.
# so we don't have to write any self argument.

print(emp3.pay)
print(emp4.pay)


"""Here what is happening behind the scene?
   self is a keyword.
   when we built constructers and an object like this one-
   python thinks that,
   self=emp1
   so "self.first" refers to"emp1.first"
   """

# if we want to print the full name of an employee.
# we can do it manually outside our class.
print(f"{emp3.first},{emp3.last}")

# but let ignore this bunch of code and go to our class and make a method which will handle this task easily.
class Employee2:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last      
        self.pay=pay
        self.email=first +"."+last+"@company.com"
    def fullname(self):                           # here note that, we need to add "self" arguement to every method we want to add in the class.
        return f"{self.first} {self.last}"

emp5=Employee2("zinedin","zidan",3000)
emp6=Employee2("sergio","ramos",4000)

print(emp5.fullname()) # remember we have to use brackets after fullname. Because it is a method not an attribute.
#or-
print(Employee2.fullname(emp6))