'''
     elif :- these kind of statement are used to check several conditions simultaneously.
            if any of the condition is true it executes the block.
        syntax :-
          if (condition):
              block of code
          elif (condition):
              block of code
          else (condition):
              block of code
'''

a=7
b=9
c=11

if a>b & a>c :
    print(a,"is greator than",b,"and ",c)
elif b>a & b>c:
    print(b,"is greator than",a,"and ",c)
else:
    print(c,"is greator than",a,"and",b)