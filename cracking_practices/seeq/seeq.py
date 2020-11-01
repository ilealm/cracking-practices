# From Jason Rust to Everyone: (1:06 PM)
# In this small coding challenge, the intent is to verify your understanding of the basics of Object Oriented Programming.

# Please define a 2-D geometry library that allows you to calculate total area for a list of objects.

# For example, I may want to instantiate a Circle, two Rectangles and a Triangle and then find out what the total area is.

# The objects do not need to be able to represent their X-Y location in a 2-D space.

# INPUTS
# circule pi r^2  => "circule", r
# rectanble :w x h => = "rectangle" 3 x 4
# triangle .5 x base x h => "triangle", b= 3, h =>

# OUTPUT
# r =2 ,=>  12.26
# w =3, h=4 => 12
# base = 3, h=2 => 3
# =>27.56

# EDGE CASES
# I can receive any figure, any times


class Geometry:
    def __init__(self):
        pass

    class Circule:
        def __init__(self, radious):
            self.radious = radious

        def get_area(self):
            return 3.14 * (self.radious * self.radious)

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def get_area(self):
            return self.width * self.height

    class Triangle:
        def __init__(self, base, height):
            self.base = base
            self.hight = height

        def get_area(self):
            return 0.5 * self.base * self.hight


# This is another approach, where each figure inherit from main class Geometry,
# and I use a class variable to have track of all the geometry obj that have been
# created


class Geometry_v2:
    total_obj_area = 0  # class variable, so I can have track of the area sum

    def __init__(self):
        pass

    # this method will be called every time a child has been created.
    def child_created(self):
        self.add_total_obj_area(self.area)

    # I can assume all childs have a area variable
    def add_total_obj_area(self, area):
        Geometry_v2.total_obj_area += area

    def get_total_objs_area(self):
        return Geometry_v2.total_obj_area


class Circle(Geometry_v2):
    def __init__(self, radious):
        self.radious = radious
        self.area = 3.14 * (self.radious * self.radious)

        Geometry_v2.child_created(self)

    def get_area(self):
        return self.area


class Rectangle(Geometry_v2):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.width * self.height

        Geometry_v2.child_created(self)


    def get_area(self):
        return self.area


class Triangle(Geometry_v2):
    def __init__(self, base, height):
        self.base = base
        self.hight = height
        self.area = 0.5 * self.base * self.hight

        Geometry_v2.child_created(self)


    def get_area(self):
        return self.area


if __name__ == "__main__":

    circle = Geometry.Circule(2)
    rec = Geometry.Rectangle(3,4)
    trian = Geometry.Triangle(3,2)

    geometry_list = []
    geometry_list.append(circle.get_area())
    geometry_list.append(rec.get_area())
    geometry_list.append(trian.get_area())

    sum = 0
    for g in geometry_list:
        sum += g

    print('The values of the objects on versio 1 is',sum)

    # VERSION 2
    all_figures = Geometry_v2()
    circle = Circle(2)
    rec = Rectangle(3,4)
    trian = Triangle(3,2)

    print('The values on all the objects on Geometry_v2 is', all_figures.get_total_objs_area())


