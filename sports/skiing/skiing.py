class Sport:
    def __init__(self, type, location, equipment): # function
        self.a = type                      # instance variable
        self.b = location                  # instance variable
        self.c = equipment                 # instance variable
        
    def Equipment(self):
        print(self.a)
        print(self.b)
        print(self.c)
        print("----------------------------------------------------------") 
        print(self.a + ' is a good sport')
        print(self.c + ' are very important piece of equipment for '+ self.a)
        print(self.b + ' is the least intresting destination for ' + self.a)
                      
sport_1 = Sport('skiing','France','Skis')
print("*****************************************************************")
sport_1.Equipment()
print("=================================================================")
sport_2 = Sport('Archery', 'Isreal', 'Bow & arrows')
sport_2.Equipment()


#sport_1 = Sport('Skiing','France', 'Skis')                   # Object
#sport_2 = Sport('sprinting','United kingdom', 'spike boots') # Object
#print(sport_1.a)
#print(sport_2.a)
#print(sport_1.b)
#print(sport_2.b)
#print(sport_1.c)
#print(sport_2.c)
#print(snow_sport.__dict__)
#print(race_sport.__dict__)