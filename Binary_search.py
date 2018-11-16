n=input("Enter no. of inputs")
arr=[]
print("Start entering your nos.")
for i in range(int(n)):
    arr_items=int(input())
    arr.append(arr_items)
k=int(input("Enter the elements u wanna search "))
def Binary_search_iterative(arr,k):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if k==arr[mid]:
            return True
        elif k<arr[mid]:
            high=mid-1
        else :
            low=mid+1
    return False
x=Binary_search_iterative(arr,k)
if x==False:
    print("Your no. is not present in the array inserted\n")
else:
    print("Your is not present in the array inserted\n")

