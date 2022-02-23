'''
    they let you define number of arguments for a function
      this is done using the asterisk symbol

      when it has one asterisk all the positional arguments are collected as tuple/
      when it has two asterisk all the positional argument from starting to end are treated as dictionary.
'''

def total_numbers(a=7,*number,**phonebook):
    print("my favorite number is ", a)

    for num in number:
        print("num ", num)
    for name,phone_number in phonebook.items():
        print(name,phone_number)

total_numbers(7,1,2,3,Jane=1234,John=5678,Jown=9012)