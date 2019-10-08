# opp_extra 
# combining multiple classes and object.
class Robot :
    def __init__(self,name,color,weight):
        self.name=name
        self.color=color
        self.weight=weight

    def introduce_self(self):
        print("My name is "+ self.name)

r1=Robot("Tom","red",30)
r2=Robot("Jerry","blue",40)

r1.introduce_self()
r2.introduce_self()

class Person :
    def __init__(self,name,personality,isSitting):
        self.name=name
        self.personality=personality
        self.isSitting=isSitting

    def sit_down(self):# when we run this method to any object the is sitting value will be true.
        self.isSitting=True
    def stand_up(self):# when we run this method to any object the is sitting value will be false.
        self.isSitting=False

p1=Person("Shawki","Intelligent",False)
p2=Person("Sowad","talkative",True)

# if p1 owns r2 and p2 owns r1
p1.robotOwened=r2
p2.robotOwened=r1

# now we can access this robotOwned atrribute in p1/p2 object.
p1.robotOwened.introduce_self()
p2.robotOwened.introduce_self()