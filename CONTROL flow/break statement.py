'''
    break : it is a statement that is used to break out of a loop
           it will terminate the loop even if the condition is true
           but for that to happen the break condition should be satisfied
'''

i=1

while i < 10:
    print(i)
    if i == 6:
        break
    i += 1