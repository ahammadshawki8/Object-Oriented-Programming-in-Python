# creating a class of my class.

class Science:
    form ="c"
    num_student=0

    def __init__(self,name,college_num,fav_sub):
        self.name=name
        self.college_num=college_num
        self.fav_sub=fav_sub
        Science.num_student+=1
    
    def introduce(self):
        print(f"Hey! I am {self.name}.My form is {self.form} and college number is {self.college_num}. I like {self.fav_sub} most.")

    def change_sub(self,sub):
        self.fav_sub=sub
        print("My favourite subject is {} now!".format(self.fav_sub))

    @classmethod
    def change_form(emp,form):
        emp.form=form
        print("Science C is now become Science {} ".format(emp.form))

    @staticmethod
    def school_day(day):
        if day.weekday==5 or day.weekday==6:
            return False
        else:
            return True

    def __add__(self,other):
        return self.college_num+other.college_num
    def __len__(self):
        return len(self.name)

    @property
    def print_name(self):
        print(self.name)
    
    @print_name.setter
    def print_name(self,name):
        self.name=name
        print(self.name)

    @print_name.deleter
    def print_name(self):
        self.name=None

class Hater_mkj(Science):
    def __init__(self,name,college_num,fav_sub,hate):
        super().__init__(name,college_num,fav_sub)
        self.hate=hate
    def prove(self):
        if self.hate:
            print("MKJ is the worst teacher in the world. Piss on you!")
        else:
            print("I think MKJ and ME both are foolish :(")


student1=Science("Shawki",5130,"Math")
student2=Science("Hasnine",5150,"Chemistry")
student3=Science("Arko",5162,"Math")
student4=Science("Mahidul",5139,"Physics")
student5=Science("Abir",5169,"eating")
student6=Hater_mkj("Anonymus",0000,"not chemistry",False)


student1.introduce()
student2.introduce()
student5.introduce()

print()

student3.change_sub("Physics")

print(student1.form)
print(student2.form)
print(Science.form)

student6.introduce()
student6.prove()

print(student1+student2)
print(len(student1))

student1.print_name
student1.print_name="New_name"
del student1.print_name
student1.print_name