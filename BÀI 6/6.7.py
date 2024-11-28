print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
     
        return math.pi * (self.radius ** 2)

    def circumference(self):
       
        return 2 * math.pi * self.radius
    
radius = float(input("Nhập bán kính của hình tròn: "))

circle = Circle(radius)

print("Diện tích hình tròn là:", circle.area())
print("Chu vi hình tròn là:", circle.circumference())

