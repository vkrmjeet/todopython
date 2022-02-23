'''
    else statement :- this is the secondary condition that is executed when the primary condition is not true
    similarly elif statement can be used in between the if and else statements
'''

a=5
b=6
c=7

if a>b & a>c :
    print(a,"is greator than",b,"and ",c)
elif b>a & b>c:
    print(b,"is greator than",a,"and ",c)
else:
    print(c,"is greator than",a,"and",b)