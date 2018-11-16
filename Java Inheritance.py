class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def display(self):
        print(self.width," ",self.height)
        return " "

class RectangleArea(Rectangle):
    def read_input(self,width,height):
        super(RectangleArea, self).__init__(width,height)

    def display(self):
        print(self.width*self.height)
        return " "

def main():
    m,n=map(int,input().split(" "))
    R = Rectangle(m,n)
    RA=RectangleArea(m,n)
    R.display()
    RA.display()
main()
