'''Distinct_Numbers HACKERRANK CODING CHALLENGE'''

def numberOfPairs(a, k):
    v=[]
    for i in range(0,len(a)-1):
        fix=a[i]
        for j in range(i+1,len(a)-1):
            x=[]
            if fix+a[j]==k:
                v.append(fix)
                v.append(a[j])
                x.append([v])
                break
            j+=1
    q=[]
    for s in range(0,len(v)-1):
        if v[s]==v[s+1]:
            q.append(v[s])
            break
    return len(q)

i=int(input("Enter the size of List"))
a=[]
print("Start entering your List items")
for x in range(i):
    a_item=int(input())
    a.append(a_item)
k=int(input("Enter the targeted value"))

print(numberOfPairs(a, k))