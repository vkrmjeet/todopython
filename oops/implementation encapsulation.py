class Cars():
    def __init__(self,speed,color):
        self.__speed = speed    #the __double underscore prefix makes the variable private and it cannot be accessed
        self.__color = color    #outside the class

    def set_speed(self,value):  #this method is used to change the value of self.speed
        self.__speed = value

    def get_speed(self):
        return self.__speed

    def set_color(self,value):
        self.color = value
    def get_color(self):
        return self.color

maruti = Cars(110,"grey")

print(maruti.get_speed())
maruti.set_speed(200)   #THIS  will set the speed to 200
print(maruti.get_speed())
maruti.speed=250    #this cannot set the speed to 250 as the variable is private and it cannot be accessed directly
print(maruti.get_speed())
                    #to change 