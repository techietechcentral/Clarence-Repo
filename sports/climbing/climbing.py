class Sport:
    def __init__(self, type, equipment):   # initialization function
        self.a = type                       # instance variable       
        self.b = equipment                 # instance variable

    def equipment(self):
       print(self.b + ' are very important piece of equipment for '+ self.a)
        
sport_1 = Sport('climbing','ropes')
sport_1.equipment()
print("=======================================================")    
sport_2 = Sport('Skiing','Skis')
sport_2.equipment()
print("=======================================================")                   
sport_3 = Sport('sprinting','spike boots')         
sport_3.equipment()
print("=======================================================") 
print(sport_1.a)
print(sport_1.b)
print(sport_2.a)
print(sport_2.b)
print(sport_3.a)
print(sport_3.b)
print("------------------------------------------------------")   
#print(snow_sport.__dict__)
#print(race_sport.__dict__)
