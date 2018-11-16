n=input("Enter the no. of inputs")
arr=[]
print("Start entering your list elements")
for i in range(int(n)):
    arr_items=input()
    arr.append(arr_items)
print(arr)
arr=' '.join(arr)
print(arr)