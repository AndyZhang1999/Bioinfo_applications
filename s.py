import math
class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.radius = r

    def perimeter(self):
        return 2*3.14*self.r

    def area(self):
        return math.pi*(self.radius**2)
circle = Circle(-3, 3, 5)
class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def shortest_distance_to_circle(self, circle):
        if isinstance(circle, Circle):
            pass
        else:
            quit(f'{circle} is not a instance of Circle, cannot compute')
        # if circle.x == 0 and circle.y == 0:
        #     distance = abs((self.x**2 + self.y**2)**(1/2) - circle.radius)
        # elif:
        distance = abs(((self.x - circle.x) ** 2 + (self.y - circle.y) ** 2) ** (1 / 2) - circle.radius)
        return round(distance, 2 - int(math.floor(math.log10(abs(distance)))) - 1)
point = Point(-2, 0)
print(point.shortest_distance_to_circle(circle))
