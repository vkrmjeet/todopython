'''

'''

def addnumber(a,b,c = 0,d=0,e = 0):
    return a+b+c

print(addnumber(1,2))
print(addnumber(3,3,3))

class Numbers:
    def __init__(self,a = 0 , b = 0 ,c =0):
        self.a=a
        self.b=b
        self.c=c
    def numbers(self):
        print(self.a+self.b+self.c)

a=Numbers(2,3,4)
a.numbers()

b=Numbers(1)
b.numbers()

class UK():
    def capital_city(self):
        print("london is the capital city of Uk")
    def language(self):
        print("English is the primary language")

class UK():
    def capital_city(self):
        print("Madrid is the capital city of Spain")
    def language(self):
        print("Spanish is the primary language")