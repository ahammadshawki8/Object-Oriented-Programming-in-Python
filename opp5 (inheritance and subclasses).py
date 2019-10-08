# opp5
# inheritance and subclasses.

# inheritance allows us to inherit attributes and methods from a parent class. 
# this is useful because we can create subclasses and get all the functionalitiey of our parent class,
# and then we can overwrite or add completely new functionality without affecting parent class.

# now lets create different types of employees.
# lets say we wanted to create developers and managers.
# here we need to use subclasses.
class Employee:
    raise_amount=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+last+"@gmail.com"
    def fullname(self):
        return f"{self.first} {self.last}"
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)

# making a subclass
class Developer(Employee):# here we are using the parent class name in the brackets,
    pass                  # to specify which parent class' functionality we want to inherit.

# here our subclass dont have any code of its own.
# but this subclass will have all the attributes methods of our Employee class.

dev_1=Employee("ahammad","shawki",200)
dev_2=Employee("cristiano","ronaldo",400)

print(dev_1.email)
print(dev_2.email)

# it will also work if we create our object in Developer subclass
dev_1=Developer("ahammad","shawki",200)
dev_2=Developer("cristiano","ronaldo",400)

print(dev_1.email)
print(dev_2.email)

# whats happen here?
# when we instantiated our Developers it first looked in our Developers subclass for constructer.
# and its not going to find it in our developer class because it's currently empty.
# so what python is going to do then is walk up a chain of inharitance until it finds what it is looking for.
# this chain called "method resoulution order"

# we can visulize that by help function.
#print(help(Developer))
# here we can see that-
"""Method resolution order:
Developer
Employee      
builtins.object"""
# so when we create a new developer object it first look in our developer subclass for constructer.
# if it didn't find it there then search in the Employee parent class.
# if it didn't find it there also the last place that it would have looked is this bulitins.object class.
# every class in python inherits from this base bulitins.object class.

# we can also know by help method that our subclass has inherited all the variable and methods from the parent class for free.

# now we want to customize our subclass.
# and we are going to change the raise_amount for our developers.
# but first lets see what happens when we apply raise_amount function to our current developers.
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
# lets say we want our developers to raise amount of 1.10
# we can do this by-
class Developer2(Employee):
    raise_amount=1.10
dev_3=Developer2("sergio","ramos",500)

print(dev_3.pay)
dev_3.apply_raise()
print(dev_3.pay)

# now python using our developer subclass raise amount instead of parent class raise amount.

# actually by changing the raise_amount and our subclass dont effect on any of our employee parent class.
# so we can make this kinds of changes of our subclasses without worrying about breaking anything in the parent class. 
dev_4=Employee("gerath","bale",800)  

print(dev_4.pay)
dev_4.apply_raise()
print(dev_4.pay)

# sometimes we need to initiate our subclasses with more information than our parent class can handle.
# lets say we want to add an extra attribute for our developers which is their main programming language.
# but currently our parent class doesn't contain that attribute.
# so to pass an additional attribute for our developers subclass, we need to give the subclass its own constructer.
# so we can do this-
class Developer3(Employee):
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)# here we don't need to write all the code like self.pay=pay etc.
        self.prog_lang=prog_lang
# instead of doing that we will let our parent class to handle first, last and pay attribute.
# we will let developer to set the prog_lang attribute.
# so in order to let our parentclass to handle previous attribute, we can write-
# super().__init__(first,last,pay)
# here super is a function which allows us to do this.
# in the brackets after init we dont have to write self as our first arguement.
# now we handled the prog_lang just like old tecnic.

dev_5=Developer3("luca","modrich",300,"ruby")
dev_6=Developer3("neymar","jr.",900,"java")

print(dev_5.email)
print(dev_5.prog_lang)

# lets make a new subclass called manager.
class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):# here we don't use empty list for our default employees value.
        super().__init__(first,last,pay)             # because we should not pass any mutable datatype like empty list or dictionary.
        if employees is None:                        # instead of that we use None and do some extra coding to make sure that our code is error free.
            self.employees=[]
        else:
            self.employees=employees
# add a employee           
    def add_emp(self, emp):    
        if emp not in self.employees:
            self.employees.append(emp)
# remove a employee
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
# print out the fullnames of employees
    def print_emp(self):
        for emp in self.employees:
            print("-->",emp.fullname())
man_1=Manager("zinedin","zidane",100,[dev_1])

print(man_1.email)
man_1.add_emp(dev_2)
man_1.add_emp(dev_3)
man_1.remove_emp(dev_1)
man_1.print_emp()

# so now we know thw importance of subclass?
# => here the code for all of our developers and managers is specific.
# => and they dont create problem with each other.
# => and we can inherit all the properties of parent class to our subclass by a single line of code.
# => so we are really getting reuse our code nicely here if we use subclasses.

# python has two buit_in function called isinstance and issubclass.

# is instance will tell us if an object is an instance of a class.
print(isinstance(man_1,Manager))
print(isinstance(man_1,Employee))
print(isinstance(man_1,Developer))
# here we need to enter two arguement.
# first one is the instance and the second is the class.

# is subclass will tell us if it is a subclass of a class.
print(issubclass(Developer,Employee))
print(issubclass(Manager,Employee))
print(issubclass(Manager,Developer))
# here we need to enter two arguement.
# first one is the subclass and the second is the parent class.