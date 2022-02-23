for _ in range(int(input())):
    n = int(input())
    lis = list(map(int,input().split()))
    res = sum(lis)
    if res%2==0:
        print(1)
    else:
        print(2)