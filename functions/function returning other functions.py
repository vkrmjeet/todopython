def greeting():
    def say_hello():
        return "hello bro"
    return say_hello


hello= greeting()
print(hello())      #this will print the return value of say hello