def Bubble_sort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j + 1]=arr[j+1], arr[j]
            return arr
n=input("Enter no. of inputs")
arr=[]
print("Start entering your nos.")
for i in range(int(n)):
    arr_items=int(input())
    arr.append(arr_items)
print(Bubble_sort(arr))
