
class UK():
    def capital_city(self):
        print("london is the capital city of Uk")
    def language(self):
        print("English is the primary language")

class Spain():
    def capital_city(self):
        print("Madrid is the capital city of Spain")
    def language(self):
        print("Spanish is the primary language")

queen = UK()
#queen.capital_city()
#queen.language()

spain = Spain()
#spain.capital_city()
#spain.language()

for country in (queen,spain): #for loop can be used to iterate through the instances
    country.capital_city()
    country.language()

#polymorphism can be created by using existing method on a new function
def europe(eu):
    eu.capital_city()
europe(queen)  #this will print the capital city of the function from which the object queen is created
europe(spain)