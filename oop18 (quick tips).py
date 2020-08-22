# OOP quick tips

# Tip 1
# printing the children classes of Parent class.
# Parent classes
class Father:
    def __init__(self):
        value=0

    def update(self):
        value+=1

    def renew(self):
        value=0

    def show(self):
        print(value)

class Mother:
    def __init__(self):
        value=1

    def update(self):
        value-=1

    def renew(self):
        value=0

    def show(self):
        print(value)


# Children classes
class Child_1(Father):
    def update(self):
        value+=2

class Child_2(Mother):
    def update(self):
        value-=2
        

# the main function.
def interiors(*classx):
    subclasses=set()
    work=[*classx]
    while work:
        parent=work.pop()
        for child in parent.__subclasses__():
            if child not in subclasses:
                subclasses.add(child)
                work.append(child)

    return subclasses

print(interiors(Father,Mother))



