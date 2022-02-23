'''
b = "Hello"

print(int(b))  this will show error
'''

while True:
    try:
        n = int(input("Enter a whole number : "))
        break
    except ValueError:
        print("Entered value should be a whole number")

print("great you entered an integer")