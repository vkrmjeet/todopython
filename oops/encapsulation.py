'''
    it is the process of restricting access.
    it prevents direct data modification of methods and variables
    public methods and variables can be accessed anywhere in the program
    private methods and variables can be accessed anywhere in the class
'''

class Cars():
    def __init__(self,speed,color):
        self.speed = speed
        self.color = color

    def set_speed(self,value):  #this method is used to change the value of self.speed
        self.speed = value

    def get_speed(self):
        return self.speed

    def set_color(self,value):
        self.color = value
    def get_color(self):
        return self.color

maruti = Cars(110,"grey")
hyundai = Cars(120,"black")
mahindra = Cars(150,"white")

print(maruti.get_speed())
maruti.set_speed(200)   #THIS  will set the speed to 200
print(maruti.get_speed())
maruti.speed=250    #this will set the speed to 250
print(maruti.get_speed())
                     #without any kind of enapsulation the data can be easily edited

print(maruti.get_color())
maruti.set_color("yellow")
print(maruti.get_color())