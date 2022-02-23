for _ in range(int(input())):
    n=int(input())
    c=0
    j=5
    while(n/j>=1):
        c = c + int(n/j)
        j = j*5
    print(c)
'''
6
3
60
100
1024
23456
8735373
'''