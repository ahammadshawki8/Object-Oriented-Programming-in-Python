# opp2
# class variables

# what is class variables?
# class variables are variables that are shared among the attributes of a class.
# while instance variables are unique to each other, class variable should be the same for each attributes.

class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    def fullname(self):
        return f"{self.first} {self.last}"
    def apply_raise(self):
        self.pay=int(self.pay*1.04)
emp1=Employee("ahammad","shawki",200)
emp2=Employee("cristiano","ronaldo",400)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay) 

# in this code, we are calculating the raise amout of employee.
# it is good but not great
# if we want to change the amount, we have to change it manually several times in several places.
# we can rather use a class variable. 

class Employee2:
    raise_amount=1.04  # here we are setting our class variable.

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    def fullname(self):
        return f"{self.first} {self.last}"
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)# in order to access our class variable, we need to write self before the variable name.
    #or self.pay=int(self.pay*Employee.raise_amount)  pp# we can also write the class name before the variable name.
    # but this two cases have difference? 

emp1=Employee2("ahammad","shawki",200)
emp2=Employee2("cristiano","ronaldo",400)

print(emp2.pay)
emp2.apply_raise()#applying the function on emp2 
print(emp2.pay)

# here to know actually what is going on, we are writing some additional code
print(Employee2.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
# we can access the class variable from both the class and the attributes

# how to print the emp1 info in a dictionary
print(emp1.__dict__)
# there is no raise_amount in the list.

# now we print out the Employee2 class.
print(Employee2.__dict__)
# this class contains the raise_amount attribute.

# when we running the code in line 34, python first search to access the raise_amount from the object.
# if it doesnt find any attribute,
# it will access the raise_amount from the Employee2 class.

# When we update the raise_amount outside/of our class, the raise_amount will automatically updated in all attributes.
Employee2.raise_amount=1.05
print(Employee2.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print("\n\n")

# but when we change the raise_amount of any attribute, it only changes the raise amount of that specific attribute.
emp2.raise_amount=1.09
print(Employee2.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# why did it do that?
# when we made that assingning it actually created the raise_amount attribute within the emp2.
# so now we have a raise amount arrtibute in emp2.
# it is not longer a class variable for emp2, it is a attribute.
print(emp2.__dict__)
# so if python finds the attribute in the object,
# it wont access it from the class.

Employee2.raise_amount=1.08
print(Employee2.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
# here we have again change the class variable from the class,
# but emp2 has raise_amount still 1.09 as it has made its own property(attribute)

# so we should write "self.raise_amount" rather than "Employee.raise_amount"
# because it gives us flexibility to update our raise_amount in any object later.
# it also allowed any subclass to overwrite that constant if we wanted to.

# now lets look another example of class variable wfere it wouldn't really make sense to use self.
# lets say we wanted to keep track how many employee we have.
# so the number of employee should be the same for all our class and object
class Employee3:
    numemp=0 # each time we created a new employee it will increase
    raise_amount=1.04  

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        Employee3.numemp +=1  # we are going to do that in our constructer. because it runs everytime when we create a new employee.
    # here we must use "Employee3" istead of "self"
    # because in the previous case we can think about that we may need to overridden the class variable.
    # but in this case there"s no use case we can think of where we want our total number of employees to be different for any one attribute.
    
    def fullname(self):
        return f"{self.first} {self.last}"
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)

print(Employee3.numemp)# it will give us zero because we have not make any object yet.

emp1=Employee3("ahammad","shawki",200)
emp2=Employee3("cristiano","ronaldo",400)

# now, we print out the number of employee
print(Employee3.numemp)# it will give us two beceuse it has raised two times.

# in attribute we need to write self.
# and we can call them by object.

# in class variable we can write both class and object.
# we can call by both class and object.
