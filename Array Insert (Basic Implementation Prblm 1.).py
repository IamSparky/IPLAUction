"""Array Insert"""
print("Enter the length of the array and no. of queries to be operated")
x, y = input().split(" ")

global arr
arr = []

print("Start entering your inputs acc. to array length")
arr=map(int,input().split(""))

def First_query(position,item):
    for i in range(0,len(arr)-1):
        if i==position:
            arr[i]=item
    return arr

def Second_Query(start_pos,end_pos,l):
    s=0
    for z in range(start_pos,end_pos+1):
        s=s+int(l[z])
    return s

for i in range(int(y)):
    a,b,c=map(int,input().split(" "))

    if a == 1:
        array=First_query(b,c)
        print(array)
    elif a == 2 :
        print(Second_Query(b,c,arr))

