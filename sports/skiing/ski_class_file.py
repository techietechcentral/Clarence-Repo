#class Employee:
"""docstring: Class tutorial using employee class. 
Here we try first figure out the special characteristics of Employee
in relation to data and build attributes. This is same for are class which we must
habe to create"""
    #pass
    #def __init__ (self, first, last, employeeID, salary):
        #self.first = first
        #self.last = last
        #self.employeeID = employeeID
        #self.salary = salary


#emp_1 = Employee('Mike', 'Okoye', 34211, 45990) # instances of the employee class
#emp_2 = Employee('Mary', 'Luka', 56661, 67000) # instance of the employee class

#print(emp_1)
#print(emp_2)

#emp_1.first ='Tom'          # instance variable
#emp_1.last ='Baker'         # instance variable
#emp_1.employeeID = 23546    # instance variable
##emp_1.salary = 50000        # instance variable

#emp_2.first ='Teem'         # instance variable
#emp_2.last ='Taker'         # instance variable
#emp_2.employeeID = 23547    # instance variable
#emp_2.salary = 55000        # instance variable

#print(emp_1.employeeID)
#print(emp_2.employeeID)
class Sport:
    def __init__(self, type, location, equipment): # function
        self.a = type                      # instance variable
        self.b = location
        self.c = equipment                 # instance variable
    def equipment(self):
        print("Skis are very important equipment for "+ self.a)       
hdware = Sport('skiing','France','Skis')
hdware.equipment()



snow_sport = Sport('Skiing','France', 'Skis') # Object
race_sport = Sport('sprinting','United kingdom', 'spike boots') # Object

print(snow_sport.a)
print(race_sport.a)
print(snow_sport.b)
print(race_sport.b)
print(snow_sport.c)
print(race_sport.c)
#print(snow_sport.__dict__)
#print(race_sport.__dict__)



    
     

#def equipment(self):
 #       pass
#class Student:
    #pass
#x = Student()
#print(dir(x))

#import turtle

#class Polygon:
    #def __init__(self, sides, name):
        #self.sides = sides
        #self.name = name
    #def draw(self):
        #for i in range(self.sides):
            #turtle.forward(100)
            #turtle.right(-72)
        #turtle.done()


#square = Polygon(4,'Square')
#pentagon = Polygon(5,'Pentagon')

#print(square.sides)
#print(square.name)

#print(pentagon.sides)
#print(pentagon.name)

#pentagon.draw()
