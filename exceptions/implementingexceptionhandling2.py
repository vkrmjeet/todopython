while True:
    try:
        n = 12 / int(input("Enter a whole number : "))
        print("the value of your number is", n)
    except ZeroDivisionError as e:
        print("you cannot divide by zero")
    except ValueError as e:
        print("please enter an integer")
    finally:
        print("Hope you entered a whole number.")