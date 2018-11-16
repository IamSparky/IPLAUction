class Bridge_Construction:
    def bridge_problem(self,arr):
        for j in range(1, len(arr)):
            for k in range(j - 1, -1, -1):
                if arr[k] > arr[k + 1]:
                    arr[k], arr[k + 1] = arr[k + 1], arr[k]
                else:
                    break

        arr_result = []
        s = 0
        for l in arr:
            s += l
            arr_result.append(s)

        for x in range(1, len(arr_result)):
            print(arr_result[x])
        return " "

def main():
    n = int(input())
    ar = []
    for i in range(n):
        x = int(input())
        ar.append(x)
    BC=Bridge_Construction()
    BC.bridge_problem(ar)

if __name__=='__main__':
    main()