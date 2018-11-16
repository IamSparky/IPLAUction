n=input("Enter the no. of test cases\n")
print("enter the two strings for checking Anagram\n")
c,d=0,0
for i in range(int(n)):
    p=input()
    q=input()
    a=list(p)
    b=list(q)
    for item in a:
        if item in b:
            continue
        else:
            c+=1

    for item1 in b:
        if item1 in a:
            continue
        else:
            d+=1
    print("The no. of elements to be deleted= ",c+d)