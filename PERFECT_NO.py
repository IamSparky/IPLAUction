n=int(input("Enter the no. of test cases"))
print("Start entering the numbers")
for i in range(n):
    m=int(input())
    sum=0
    for j in range(1,int(m/2+1)):
        if m%j==0:
            sum=sum+j
    if sum==m:
        print("true")
    else:
        print("false")
