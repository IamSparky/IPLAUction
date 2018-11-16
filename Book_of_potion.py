n=input("Enter your 10 digit no.\n")
m=len(n)
if m!=10:
    print("The no. entered is Invalid")
else:
    a=list(n)               #converting string n into the list a
    c=[]
    for q in a:
        c.append(int(q))    #adding string n into the new list c
    b=0
    i=1                     #initializing counter i
    if i!=11:
        for j in c:
            b = b + j * i   #adding values to the variable b
            i+=1
    if b % 11 == 0:         #checking if the varible is divisible by 11 or not
        print("Legal ISBN")
    else:
        print("Illegal ISBN")




