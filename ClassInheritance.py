class Player:
    def __init__(self,name,sport):
        self.n=name
        self.s=sport
    def message(self):
        print("The player name is ",self.n," plays ",self.s)
        return (" ")
p=Player("Maria Sharapova","Tennis")
print(p.message())