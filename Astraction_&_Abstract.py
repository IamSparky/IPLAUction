class Flights:  #A class without any complete implementation is called Abstract Class
    pass

class Indigo(Flights): #single Inheritance
    def Symbol(self):
        print("Blue in colour")

class Air_asia(Flights):
    def Symbol(self):
        print("Red in colour")

I=Indigo()
I.Symbol()

A=Air_asia()
A.Symbol()
