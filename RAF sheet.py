class Employee:
    num_emp=0
    raise_amount=1.05
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        Employee.num_emp +=1
    def apply_raise(self):
        self.pay=self.pay*self.raise_amount
    @classmethod
    def set_raise(cls,amount):
        cls.raise_amount=amount
    @classmethod
    def form_str(cls,str_emp):
        first,last,pay=str_emp.split("-")
        return cls(first,last,pay)
    @staticmethod
    def is_weekend(day):
        if day.weekday==5 or day.weekday==6:
            return True
        else:
            return False
    def __repr__(self):
        return f"Employee({self.first},{self.last},{self.pay})"
    def __str__(self):
        return f"{self.fullname()} - {self.email}"
    def __add__(self,other):
        return self.pay+other.pay
    def __len__(self):
        return len(self.fullname())
    @property
    def email(self):
        return f"{self.first}{self.last}@gmail.com"
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    @fullname.setter
    def fullname(self,name):
        first,last=name.split(" ")
        self.first=first
        self.last=last
    @fullname.deleter
    def fullname(self):
        print("name deleted!")
        self.first=None
        self.last=None

class Developer(Employee):
    raise_amount=1.10
    def __init__(self,first,last,pay,language):
        super().__init__(first,last,pay)
        self.language=language

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees==None:
            self.employees=[]
        else:
            self.employees=employees
    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_employee(self):
        for emp in self.employees:
            print("-->",emp)

    
emp_1=Employee("ahammad","shawki",1000)
emp_2=Employee("cristiano","ronaldo",2000)
str_emp1="sergio-ramos-3000"
emp_3=Employee.form_str(str_emp1)
dev_1=Developer("gerath","bale",4000,"ruby")
dev_2=Developer("keylor","navas",5000,"java")
man_1=Manager("zinedin","zidan",6000,[dev_1,dev_2])

print(Employee.num_emp)
print(emp_3.email)
import datetime
a=datetime.date(2018,12,12)
print(Employee.is_weekend(a))
print(dev_2.email)