# oop4
# static method

# regular methods in a class automatically pass attribute as a argument as the first arguement. By convention, we call it "self" 
# class methods in a class automatically pass class as a arguement as the first arguement. By convention, we call it cls.
# static methods in a class don't pass any arguement automatically. They pass neither the attribute nor the class.
# static function behave just like regular functions except we include them in our class because they have some logical connections with the class.

class Employee:
    num_emp=0
    raise_amount=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+last+"@gmail.com"
        Employee.num_emp +=1
    def fullname(self):
        return f"{self.first} {self.last}"
    def apply(self):
        self.pay=int(self.pay*self.raise_amount)
    @classmethod
    def set_raise(cls,amount):
        cls.raise_amount=amount
    @classmethod
    def str_name(cls,emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last ,pay)

    # suppose, we want to know if the day is weekday or not in our class.
    # it is logically connected to Employee class.
    # but it does not depends on class or attributes.
    # so we need to create a static method which tells us it is a weekday or not.

    @staticmethod # to create a static method we need to use this decorator
    def workday(day):
        if day.weekday()==5 or day.weekday()==6: # in python monday is numbered 0, sunday is numbered 6 and so on.
            return False                         # here day.weekday() function is used to refer to days of the week in the function.
        else:
            return True

emp1=Employee("ahammad","shawki",1000)
emp2=Employee("shakil","abrar",2000)

import datetime
my_date=datetime.date(2016,7,10)# this function makes our date read-able for python.
#or my_date=datetime.datetime.strptime("2016,7,10","%Y,%m,%d").date()
print(Employee.workday(my_date))# we need to write Employee before calling static method.

# how to be sure that it is a class method or a static method?
# if anywhere in the method we need to use cls variable that is definitely class method.
# if anywhere in the method we need to use self variable that is definitely regular method.
# otherwise, it is a static method.

# in regular method we need to write self.
# and we can call them by object. 

# in class method we need to write cls.
# and we can call them by class.

# in static method we need to write nothing.
# and we should call them by class.
