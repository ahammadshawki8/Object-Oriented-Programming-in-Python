# opp7
# property decorator

# property decorator allows us to give our class attributes getter,setter and a deleter functionality.
class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+last+"@gmail.com"
    def fullname(self):
        return f"{self.first} {self.last}"

emp_1=Employee("ahammad","shawki",10000)

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())
# here we have printed what we have expected.
# now we are going to update our first name and again do the same actions.
emp_1.first="jim"
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())
# but it prints the previous email which we haven't expected.
# now what should we do in this situation?
# here property decorator is useful.
# it allows us to define a method that we can access it like an attribute.
class Employee2:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        
    def fullname(self):
        return f"{self.first} {self.last}"
    def email(self):# so right now this method is simmilar to fullname method.so each time we ran it it will access the current first and last name.
        return f"{self.first}{self.last}.@gmail.com"

emp_2=Employee2("ahammad","shawki",10000)
emp_2.first="jim"
print(emp_2.first)
print(emp_2.email())# but now as email is a method so we need to use brackets.
print(emp_2.fullname())
# so if anyone is using our class they have to change their code also.
# but we dont want to do that.
class Employee3:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    @property    
    def fullname(self):
        return f"{self.first} {self.last}"
    @property   # it is a property decorator.it is defining the email method of our class like a attribute. 
    def email(self):
        return f"{self.first}{self.last}.@gmail.com"

emp_3=Employee3("ahammad","shawki",10000)
emp_3.first="jim"
print(emp_3.first)
print(emp_3.email)
print(emp_3.fullname)
# so in order to accessing email like an attribute.
# we can just add a property decorator above that method.
# we can do this fullname as well.

class Employee4:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    @property    
    def fullname(self):
        return f"{self.first} {self.last}"
    @property    
    def email(self):
        return f"{self.first}{self.last}.@gmail.com"

    @fullname.setter# it is a setter
    def fullname(self,name):# here we need to create another method with the same name.
        first,last=name.split(" ")
        self.first=first
        self.last=last
    

emp_4=Employee4("ahammad","shawki",10000)
emp_4.fullname="jim headings"
print(emp_4.first)
print(emp_4.email)
print(emp_4.fullname)
# here we change our fullname.
# lets say we wanted to change our first, last, email by changing our fullname.
# if we just change this property decorator without doing any additional code it will give us an error 
# in order to do that error-free, we are going to use a setter.
# it is another decorator.
# the name we are going to use for our setter is going to be the name of the property. 

# we can also make a deleter in the same way.
# if we want to delete the fullname of our employee we have to run some clean up code. so to do this,
# we are going to do the same action as setter but instead of setter it will going to be deleter.
class Employee5:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    @property    
    def fullname(self):
        return f"{self.first} {self.last}"
    @property    
    def email(self):
        return f"{self.first}{self.last}.@gmail.com"
    @fullname.setter
    def fullname(self,name):
        first,last=name.split(" ")
        self.first=first
        self.last=last

    @fullname.deleter# it is a deleter
    def fullname(self):
        print("name deleted!")
        self.first =None
        self.last =None

emp_5=Employee5("ahammad","shawki",10000)
emp_5.fullname="jim headings"
print(emp_5.first)
print(emp_5.email)
print(emp_5.fullname)

# deleter code is useful if we want delete an attribute.
del emp_5.fullname
# when we run this code it set our first and last attribute to none value.

# property decorator are also use to make an attribute read-only.
# if we there is a method in the class with the same name of an attribute,
# then if we use property decorator and run that, the function will be executed not the attribute.
# so the attribute become an read_only attribute. 