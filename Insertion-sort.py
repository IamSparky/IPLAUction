def Insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i-1,-1,-1):
            if arr[j]<[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            else:
                break
    return arr
n=input("Enter no. of inputs")
arr=[]
print("Start entering your nos.")
for i in range(int(n)):
    arr_items=int(input())
    arr.append(arr_items)
print(Insertion_sort(arr))


