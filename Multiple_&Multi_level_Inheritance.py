class Father:
    def Msg1(self):
        print("Knows how to do buisiness")

class Mother:
    def Msg2(self):
        print("Knows how to cook food")

class Daughter(Mother,Father): #Multiple inheritance
    def Msg3(self):
        print("Knows how to work hard for study.")
class Son(Daughter):           #Multi level inheritance
    def Msg4(self):
        print("Knows how to do Gaming.")

d=Daughter()
d.Msg1()
d.Msg2()
d.Msg3()

s=Son()
s.Msg4()
s.Msg3()    #multilevel Inheritance