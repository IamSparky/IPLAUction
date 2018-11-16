n=input("Enter your array size: ")
a=[]
print("Start Entering your no. :")
for i in range(int(n)):
    arr_items=int(input())
    a.append(arr_items)

print("1.Insertion Sort")
print("2.Bubble Sort")
print("3.Quick Sort")
print("4.Linear Search")
print("5.Binary Search")

x=int(input("Enter your Choice "))

def Insetion_Sort(arr):
    for i in range(1,len(arr)):
        for j in range(i-1,-1,-1):
            if arr[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
            else :
                break
    return arr

def Bubble_Sort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-1-i):
            if arr[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return arr

def Quick_Sort(arr):
    for i in range(0,len(arr)-1):
        minIndex=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minIndex]:
                minIndex=j
        if minIndex!=i:
            arr[i],arr[minIndex]=arr[minIndex],arr[i]
    return arr


def Linear_Search(arr,k):
    for o in range(len(arr)):
        if arr[o]==k:
            return True
    return -1

def Binary_Search(arr1,k):
    t=Bubble_Sort(arr1)
    low=0
    high=len(t)-1
    while low<=high:
        mid=(low+high)//2
        if k==arr1[mid]:
           return 1
        elif k<arr1[mid]:
            high=mid-1
        else:
            low=mid+1
    return False

if x==1:
    print(Insetion_Sort(a))
elif x==2:
    print(Bubble_Sort(a))
elif x==3:
    print(Quick_Sort(a))
elif x==4:
    l=int(input("Enter the no. you want to search: "))
    y=Linear_Search(a,l)
    if y==-1:
        print("Entered element not present in the list .....")
    else:
        print("Entered element present in the list .....")
elif x==5:
    m=Bubble_Sort(a)
    l = int(input("Enter the no. you want to search: "))
    y=Binary_Search(m,l)
    if y==False:
        print("Entered element not present in the list .....")
    else:
        print("Entered element present in the list .....")
else:
    print("You have inserted an incorrect choice!")