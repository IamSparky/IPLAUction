n=input("Enter no. of inputs")
arr=[]
print("Start entering your nos.")
for i in range(int(n)):
    arr_items=int(input())
    arr.append(arr_items)
k=int(input("Enter the no. which you want to search in the array: "))
def Linear_search(arr,k):
    for i in range(len(arr)):
        if arr[i]==k:
            return i
    return -1
x=Linear_search(arr,k)
if x==-1:
    print("Your no. is not present in the array inserted\n")
else:
    print("Your no.", k, "is at: ",x, "th position in your inserted array\n")




