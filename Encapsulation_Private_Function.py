class Animal:
    def __init__(self,name1):
        self.name=name1
        self.__update()
    def say(self):
        print("It roar "+self.name)
    def __update(self):
        print("Cheetah")
a=Animal("Wrath")
a.say()