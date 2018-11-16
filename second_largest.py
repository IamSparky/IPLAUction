print("Enter the no. of elements\n")
n=int(input())
print("Start entering the nos.\n")

list1=[]
for i in range(n):
    n1 = int(input())
    list1.append(n1)
largest=list1[0]
second_largest=list1[0]
for i in list1:
    if(i>largest):
        largest=i
for i in list1:
    if(i==largest):
        continue
    if(i>second_largest):
        second_largest=i
print(second_largest)