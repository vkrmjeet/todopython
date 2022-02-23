x=int(input())
y=float(input())
if x+0.5>y:
    print(format(y,'.2f'))
elif (x%5==0):
    print(format(y-x-0.5,'.2f'))
else:
    print(format(y,'.2f'))