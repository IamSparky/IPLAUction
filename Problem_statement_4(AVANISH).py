class Employee:
    basic = 0
    da = 0
    hra = 0
    id = 0
    name = 0
    ts = 0

    def __init__(self,name,id,basic,da,hra):
        self.basic=basic
        self.da=da
        self.hra=hra
        self.id=id
        self.name=name

    def calulateSalary(self):
        self.ts=self.basic+self.da+self.hra+self.name+self.id
        return self.ts

class Hr(Employee):
    gp=0
    def __init__(self,name,id,basic,da,hra,gp):
        super(Hr,self).__init__(name,id,basic,da,hra)
        self.gp=gp

    def calulateSalary(self):
        self.ts = self.basic+self.da+self.hra+self.gp
        return self.ts



class Developer(Employee):
    ip=0
    def __init__(self,name,id,basic,da,hra,ip):
        super(Developer,self).__init__(name,id,basic,da,hra)
        self.ip=ip

    def calulateSalary(self):
        self.ts = self.basic+self.da+self.hra+self.ip
        return self.ts

def main():

    for j in range(2):
        name2 = str(input("Enter Developer's name \n"))
        id2 = str(input("Enter Developer's id \n"))
        basic2 = int(input("Enter Developer's basic \n"))
        da2 = int(input("Enter Developer's da \n"))
        hra2 = int(input("Enter Developer's hra \n"))
        ip = int(input("Enter Developer's ip \n"))

        obj2 = Developer(name2, id2, basic2, da2, hra2, ip)
        print("Total Salary= ", obj2.calulateSalary(), "\n")

    return(" ")
if __name__=='__main__':
    main()




