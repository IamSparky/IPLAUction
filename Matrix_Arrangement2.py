import numpy as np  #importing reduce function in my program

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

list(chain.from_iterable(Mat))   #converting 2D matrix to 1D using
print(Mat)

a=np.array(Mat)

for row in a:
    print(a)
