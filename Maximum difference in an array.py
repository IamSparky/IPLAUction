'''MAXIMUM DIFFERENCE OF AN ARRAY HACKERRANK CODING CHALLENGE'''


n=int(input('Enter how many no. u wanna input'))
x=[]
a=[]
print("Start entering your numbers")
for l in range(n):
    a.append(int(input()))

def max_difference(z):
    for i in range(0, len(z)):
        for j in range(i+1,len(z)):
            nex=z[j]
            if nex>z[j-1]:
                while j !=0:
                    x.append(nex-z[j-1])
                    j-=1
            for y in x:  #removing -ve elements which is not necessary also because of using max func.
                if y < 0:
                    x.remove(y)
            break

    return max(x)
print(max_difference(a))
