def HCF(x):
    if x==1 or x==2:
        return "-1"
    elif x==3 or x==4 or x==5:
        return "1 2 3"
    else:
        for i in range(x, 0, -1):
            if i % 3 == 0:
                a, c, b = i, (i / 3), i - (i / 3)
                print(int(c),int(b),a)
                return (" ")
o=[]
j=int(input("Enter the no. of test case: "))
for c in range(j):
    n = int(input("Start Entering your input: "))
    o.append(HCF(n))
print("\n")
for l in o:
    print(l)