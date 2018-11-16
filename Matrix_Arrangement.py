from functools import reduce

m=int(input("Enter No. of Rows"))   #Taking row's no. input
n=int(input("Enter No. of Columns")) #Taking column's no. input

Mat=[]       #Matrix initialization

for i in range(0,m):
    Mat.append([])        #Matrix's row initialization

for i in range(0,m):
    for j in range(0,n):
        Mat[i].append(j)  #Matrix's column initialization
        Mat[i][j]=0       #Matrix(m X n) contains 0 as initialized values

for i in range(0,m):
    for j in range(0,n):
        print('entry in row ',i+1,' column ',j+1)
        Mat[i][j]=int(input()) #taking input of matrix at i & j positions

s=reduce(lambda x,y :x+y ,Mat)
      #converting 2D matrix(Mat) to 1D using lambda and reduce functions

arr=sorted(s,reverse=True)

a=len(arr)

final1=arr[0:a:2]


final=arr[1:a-1:2]
final2=sorted(final)

print(final1+final2)

