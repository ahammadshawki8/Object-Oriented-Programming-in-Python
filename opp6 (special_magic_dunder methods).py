# opp6
# special/magic/dunder methods

# there are some methods in python we can use within our classes.
# this methods called special methods or magic methods or dunder methods.
# this special methods allow us to emulate some built_in behaviour within python and its also how we implement operator overloading.
class Employee:
    raise_amount=1.05
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+last+"@gmail.com"
    def fullname(self):
        return f"{self.first} {self.last}"
    def apply_raise(self):
        self.pay =self.pay*self.raise_amount

emp_1=Employee("ahammad","shawki",10000)
emp_2=Employee("cristiano","ronaldo",20000)

# if we print emp_1 , we find some message.
print(emp_1) 
# it is nice if we change its behaviour and print out something like user-friendly .
# these special methods are going to allow us to do that.

# special method are always sorrunded by double underscore(_)
# so for that reason, it also called dunder.
# so dunder init means __init__

# so lets look some other common special methods.
# dunder str is meant to be more of a readable representation of an object and is used as a display to the end_user.
class Employee2:
    raise_amount=1.05
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+last+"@gmail.com"
    def fullname(self):
        return f"{self.first} {self.last}"
    def apply_raise(self):
        self.pay =self.pay*self.raise_amount
    def __repr__(self):# repr is meant to be an anambiguous representation of the object and should be used for debugging ang logging and things like that.
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)
    def __str__(self):# str is meant to be more of a readable representation of an object and is used as a display to the end_user.
        return f"{self.fullname()} - {self.email}"
    def __add__(self, other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.fullname())

emp_3=Employee2("ahammad","shawki",10000)
emp_4=Employee2("cristiano","ronaldo",20000)

print(emp_3)
# now it returned a string that we specified in the repr method.
# so if we wanted to recreate this we can just copy our output.
# and its the exact same thing that we used to make our object.

# but when we make our __str__ method then it will access our str special method.
# it is a readable display for end_users.

# even we can also print dunder repr and str
print(repr(emp_3))
print(str(emp_3))
# so whats going on the background is that its directly calling  those special methods.
print(emp_3.__repr__())
print(emp_3.__str__())
# its is actually the same thing.

# so this to special methods allow us to how our object will be printed and displayed.
# so print(emp_3) first execute dunder str.
# if there is no dunder str it will run dunder repr.
# if there is no dunder repr it will then run that ugly message.
# so its a good habit thet if we create dunder str , we should create dunder repr in our class too.

# there are also many magic methods in arithmatic.
print(1+2)
# when we run this code, it will run a dunder add in background.
print(int.__add__(1,2))# here int is a default object.

# string uses their own dunder add method.
print("a"+"b")
print(str.__add__("a","b"))

# we can also add the salaries of our  employees by dunder add.
# remember that though this methods are available for our code, but thats not available for our class by default.
# so in order to make them available for our class and objects we need to do some additional coding.
# if we do not do so our code will give us error.
print(emp_3+emp_4)# to add this we need to use + instead of , 

# there also many dunder methods.
# we can find them in this description "https://docs.python.org/3/references/datamodel.html#special-method-names"

# infact, "len" is a dunder method too.
print(len("shawki"))
print("shawki".__len__())
# we can apply this to our class.
print(len(emp_3))
# it is useful when someone writing a document and needs too know how many characters the employees name will take up.
