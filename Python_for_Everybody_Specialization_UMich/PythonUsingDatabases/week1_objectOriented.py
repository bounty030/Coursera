#week 1 - chapter 14 Object Oriented Programming

#------14.1 - Object Oriented Definitions and Terminology
#an object is a self-contained code and data

#class:                 a template
#method or message:     a defined capability of a class
#field or attribute:    a bit of data in a class
#object or instance:    a particular instance of a class

#e.g.: class is dog and the different dog races would be an object


#-------14.2 - Our First Class and Object
"""
class PartyAnimal:
    x=0 #each PartyAnimal object has a bit of data

    def party(self):
        self.x=self.x + 1
        print("So far",self.x)


 #construct a PartyAnimal object and store in a variable   
an = PartyAnimal() 

an.party() #is equal to talking PartyAnimal.party(an)
an.party()
an.party()

print("Type", type(an))
print("Dir", dir(an)) #shows us the functions of the class PartyAnimal
"""

#------14.3 - Object Life Cycle
#objects are created, used and discarded
#we have special blocks of code (methods) that get called 
# (both are optional):
    #at the moment of creation (constructor)
    #at the moment of destruction (destructor)

#constructor - set up initial values
"""
class PartyAnimal:
    x=0 #each PartyAnimal object has a bit of data

    #constructor
    def __init__(self):
        print("I am constructed")

    def party(self):
        self.x=self.x + 1
        print("So far",self.x)

    #destructor
    def __del__(self):
        print("I am destructed", self.x)

 #construct a PartyAnimal object and store in a variable   
an = PartyAnimal() 

an.party() #is equal to talking PartyAnimal.party(an)
an.party()
an = 42 #an gets destructed and a new value assigned

print("an contains", an)
"""


#a class is a template and there can be different instances of the class
#with different methods

"""
class PartyAnimal:
    x=0 #each PartyAnimal object has a bit of data
    name=""

    #constructor
    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x=self.x + 1
        print(self.name, "party count",self.x)

 
s = PartyAnimal("Sally") #"Sally" is passed as "z" to __init__()
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()
"""


#--------14.4 - Object Inheritance
#Inheritance: reusing an existing class and inherit all the capabilities
#of an existing class and extending this class with new code
#to make a new class

#the new class is called child and the second class is called parent

#the new class is also called a subclass 
#e.g. the parent class is called "animal" and a subclass would be
#"dogs", "birds" ...

class PartyAnimal:
    x=0 #each PartyAnimal object has a bit of data
    name=""

    #constructor
    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x=self.x + 1
        print(self.name, "party count",self.x)


class FootballFan(PartyAnimal): #extension of PartyAnimal
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points",self.points)

s = PartyAnimal("Sally")
s.party()


j = FootballFan("Jim") #first runs PartyAnimal and then FootballFan
j.party()
j.touchdown()