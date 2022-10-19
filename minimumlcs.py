for i in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    s=set(a)
    c=0
    d=[]
    for i in s:
        if i in b:
            d.append(min(a.count(i),b.count(i)))
    if len(d)==0:
        print(0)
    else:
        print(max(d))
