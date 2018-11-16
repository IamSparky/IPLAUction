n=input()
a=[]
b=[]
c=[]
for i in range(int(n)):
    arr_item1=int(input())
    a.append(arr_item1)

for j in range(int(n)):
    arr_item2 = int(input())
    b.append(arr_item2)
print(a)
print(b)
for k in range(0,len(a)):
    for l in range(0,len(b)):
        if k==l:
            arr_item3 = a[k] + b[l]
            c.append(arr_item3)
print(c)