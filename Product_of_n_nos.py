n=int(input("Enter your array size\n"))

a=1
for i in range(n):
    p = int(input())
    a=(a*p)%((10**9)+7)
print(a)