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

# Tạo một đối tượng hình tròn với bán kính là 5
circle = Circle(5)

# Tính và in ra diện tích của hình tròn
print("Diện tích hình tròn:", circle.area())


