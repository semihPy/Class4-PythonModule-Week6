'''
#############################################################################################
#*******************************************************************************************#
#           Copyright (c) 2020 pyCoder|semih Corporation;) All rights reserved.            ##
#                                   [Timestamp:20210216]                                   ##
#*******************************************************************************************#
#############################################################################################
'''
# Create a class named Triangle and Rectangle.
# Create a subclass named Square inherited from Rectangle.
# Create a subclass named Cube inherited from Square.
# Create a subclass named Pyramid multiple inherited both from Triangle and Square.
# Two dimensional classes (Triangle, Rectangle and Square) should have:
# its dimensions as attributes.(can be inherited from a superclass)
# methods which calculate its area and perimeter separately. Three dimensional classes (Cube and Pyramid) should have:
# its dimensions as attributes which are inherited from a superclass
# its extra dimensions if there is. (hint: maybe for Pyramid)
# methods which calculate its volume and surface area separately. (surface area is optional, you may not do this)
menu = ["+===============================+",
        "|*|*|*|   SHAPE FACTORY   |*|*|*|",
        "+===============================+",
        "\t\tTriangle  --> 1",
        "\t\tRectangle --> 2",
        "\t\tSquare   ---> 3",
        "\t\tCube   -----> 4",
        "\t\tPyramid   --> 5",
        "+===============================+"]
for i in menu:
    print ('\t'.expandtabs(44), i)
class Triangle:
    def __init__(self, edge1=0, edge2=0, edge3=0):
        while True:
            try:
                self.edge1 = int(input("Enter edge1:"))
                self.edge2 = int(input("Enter edge2:"))
                self.edge3 = int(input("Enter edge3:"))
                break
            except:
                print("enter a number please!")

    def area(self):
        hp = (self.edge1+self.edge2+self.edge3) / 2
        ta = (hp*(hp-self.edge1)*(hp-self.edge2)*(hp-self.edge3))**0.5
        return ta

    def perimeter(self):
        return self.edge1+self.edge2+self.edge3

    def __str__(self):
        print(f"Triangle >>> AREA= {self.area():.1f}     PERIMETER= {self.perimeter()}")

class Rectangle:
    def __init__(self, edge1=0, edge2=0):
        while True:
            try:
                if user_choice==3 or user_choice==4:
                    self.edge1 = int(input("Enter edge1:"))
                    break
                else:
                    self.edge1 = int(input("Enter edge1:"))
                    self.edge2 = int(input("Enter edge2:"))
                    break
            except:
                print("Enter a number please!")

    def area(self):
        if user_choice==3 or user_choice==4:
            return self.edge1 * self.edge1
        else:
            return self.edge1 * self.edge2

    def perimeter(self):
        if user_choice==3 or user_choice==4:
            return self.edge1 * 4
        else:
            return (self.edge1 + self.edge2)*2

    def __str__(self):
        print("Rectangle >>> AREA= {}     PERIMETER= {}".format(self.area(),self.perimeter()))

class Square(Rectangle):
    def __init__(self, edge1=0,edge2=None):
        super().__init__(edge1, edge2)

    def __str__(self):
        print("Square >>> AREA= {}     PERIMETER= {}".format(self.area(),self.perimeter()))

class Cube(Square):
    def __init__(self,edge1=0):
        super().__init__(edge1)

    def volume(self):
        return self.edge1**3

    def __str__(self):
        print("Cube >>> SURFACE AREA= {}     VOLUME= {}".format(6*self.area(),self.volume()))

class Pyramid(Triangle, Rectangle):
    def __init__(self,edge1=0,edge2=0,edge3=0):
        super().__init__(edge1,edge2,edge3)

    def volume(self):
        return (self.edge1*self.edge2*self.edge3)*1/3

    def __str__(self):
        print("Pyramid >>> VOLUME= {0:.1f}".format(self.volume()))

while True:
    user_choice = input("Your choice: ")
    try:
        user_choice = int(user_choice)
    except:
        print("Incorrect entry. Please try again!")
    if user_choice == 1:
        print("For Triangle >>> Enter 3 edge lengths:")
        t1 = Triangle()
        t1.__str__()
    elif user_choice == 2:
        print("For Rectangle >>> Enter 2 edge lengths:")
        r1 = Rectangle()
        r1.__str__()
    elif user_choice == 3:
        print("For Square >>> Enter only 1 edge lengths:")
        s1 = Square()
        s1.__str__()
    elif user_choice == 4:
        print("For Cube >>> Enter only 1 edge lengths:")
        c1 = Cube()
        c1.__str__()
    elif user_choice == 5:
        print("For Pyramid >>> Enter 3 edge lengths:")
        p1 = Pyramid()
        p1.__str__()

    q = input("Do you want to continue (Y/N):")
    if q.upper() == 'Y':
        continue
    else:
        print("Have nice day!..")
        break
