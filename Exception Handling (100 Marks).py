n=input()
a=[]
for i in range(int(n)):
    try:
        x,y=map(int,input().split())
    except Exception:
        if x<0 or y<0:
            a.append(x," & ",y,"cannot have negative values")
        elif x==0 or y==0:
            a.append(x, " & ",y, " both cannot be zero")
    else:
        q=x**y
        a.append(q)
for j in a:
    print(j)