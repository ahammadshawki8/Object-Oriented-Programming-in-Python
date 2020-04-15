# oop3
# class methods

# regular methods in a class automatically pass attribute as a argument as the first arguement. By convention, we call it "self". 
# class methods in a class automatically pass class as a arguement as the first arguement. By convention, we call it "cls". 
class Employee:

    raise_amount=1.04  
    numemp=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        Employee.numemp +=1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)
    # to turn a regular method into a class method, we need to add a decorator to the top called @classmethod.
    # this decorator altering the functionality of our method to where now we receive the class to our first arguement.
    # by convention, we called the first arguement of our class method "cls"
    # we cant use the class as our first argument here, because the word has a different meaning in this language.
    @classmethod 
    def set_raise_amt(cls,amount): 
       cls.raise_amount=amount
    # now within this method we are going to work with class instead of object   
    
  
emp1=Employee("ahammad","shawki",200)
emp2=Employee("cristiano","ronaldo",400)

Employee.set_raise_amt(1.05)# changing the raise_amount
# this wiil change all raise_amount both class and object.
# this happens because we ran this set_raise_amt method which is a class method which means now we are working with class instead of the object.
# and we are setting that class variable raise amount equal to the amount that we passed in here which is 1.05.

# what we have done here is the same thing of saying-
Employee.raise_amount=1.05

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# we can also use class methods as alternative constructors
# it means we can use this class methods in order to provide multiple ways to creating our object.


# lets say someone is using our class.
emp_str_1 ="john-doe-700"
emp_str_2 ="steve-smith-800"
emp_str_3 ="sergio-ramos-900"
# we have three strings here that are employees separated by hyphens.

# if we want to crete new objects with this string we have to first split on the hyphen-
first, last, pay =emp_str_1.split("-")
new_emp1=Employee(first,last,pay)
print(new_emp1.pay)
# but this takes much code and time.
# so lets create an alternative constructer that allows us to pass in the string and we can create the employee.
# so lets create a new class method and we are going to use that method as an alternative constructer.

class Employee2:
    raise_amount=1.04  
    numemp=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        Employee.numemp +=1
    def fullname(self):
        return f"{self.first} {self.last}"
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)
        
    @classmethod
    def form_string(cls,emp_str):# here form is a convention.
        first, last, pay =emp_str.split("-")
        return cls(first,last,pay)# here we are using cls instead of Employee2 because cls and Employee2 are basically the same thing.

emp_str_1 ="john-doe-700"
emp_str_2 ="steve-smith-800"
emp_str_3 ="sergio-ramos-900"

new_emp1=Employee2.form_string(emp_str_1)
print(new_emp1.pay)

# characteristics of class methods:
#1. we need to add decorator @classmethod on the top of the class method.
#2. we need to add cls as the first arguement of the class method.
#3. we should use cls inside the class method.
#4. Outside the class, we should call the class method with the class name.
#5. we can use class method as alternative constructor.