'''
    continue statement : a continue statement is basically used to stop the current iteration of the loop and
                       it will continue from the next iteration
'''

i = 1

while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

