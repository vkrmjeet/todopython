for _ in range(int(input())):
    s = input()
    res = 0.0000
    p = ""
    for i in range(len(s)):
        if s[i]!='e':
            p+=s[i]
        else:
            res+=float(p)
            p=""
    if len(p)!=0:
        res+=int(p)
    print(format(res,'.4f'))