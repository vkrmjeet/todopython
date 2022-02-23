for _ in range(int(input())):
    a,b,x=input().split(" ")
    a = int(a)
    b = int(b)
    x = int(x)
    res = int((b-a)/x)
    print(res)