class imp:
    def maximum_traveling_time(self,b):
        c=0
        largest = b[0]
        second_largest = b[0]
        for i in b:
            if (i > largest):
                largest = i
        for i in b:
            if (i == largest):
                continue
            if (i > second_largest):
                second_largest = i
        for i in b:
            if i==largest:
                for i in range(largest,second_largest):
                    c=c+1
            elif i == second_largest:
                for i in range(second_largest,largest):
                    c=c+1
        print(largest+second_largest+c)
        return (" ")

def main():
    n = int(input())
    v = []
    for i in range(n):
        a = int(input())
        v.append(a)
    I=imp()
    I.maximum_traveling_time(v)

if __name__=='__main__':
    main()

