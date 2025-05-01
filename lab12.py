#Q-1
class ComplexNumber:
    def __init__(self,r,i):
        self.r =r
        self.i =i
    
    def __str__(self):
        if self.i >= 0:
            return f"{self.r} + {self.i}i"
        else:
            return f"{self.r} - {-self.i}i"

    
    def __add__(self, other):
        real_part = self.r + other.r
        imaginary_part = self.i + other.i
        return ComplexNumber(real_part,imaginary_part)

    
    def __sub__(self, other):
        real_part = self.r - other.r
        imaginary_part = self.i- other.i
        return ComplexNumber(real_part, imaginary_part)

    
    def __mul__(self, other):
        real_part = (self.r * other.r) - (self.i * other.i)
        imaginary_part = (self.r * other.i) + (self.i * other.r)
        return ComplexNumber(real_part, imaginary_part)

    
    def __truediv__(self, other):
        denominator = other.r ** 2 + other.i ** 2
        real_part = (self.r* other.r+ self.i * other.i) / denominator
        imaginary_part = (self.i * other.r - self.r * other.i) / denominator
        return ComplexNumber(real_part, imaginary_part)


num1 = ComplexNumber(4, 5)
num2 = ComplexNumber(2, -3)

print("Number 1:", num1)
print("Number 2:", num2)

print("\nAddition:", num1+num2)
print("Subtraction:", num1-num2)
print("Multiplication:", num1*num2)
print("Division:", num1/num2)

#Q-2
class Matrix:
    def __init__(self, lst=[[0,0,0],[0,0,0],[0,0,0]]):
           self.mat=lst
           
    def __add__(self, m2):
        ans=Matrix()
        for i in range(3):
            for j in range(3):
                ans.mat[i][j]=self.mat[i][j]+m2.mat[i][j]
        return ans

    def __mul__(self, m2):
        ans=Matrix()
        for i in range(3):
            for j in range(3):
                ans.mat[i][j]=self.mat[i][0]*m2.mat[0][j] + self.mat[i][1]*m2.mat[1][j]  + self.mat[i][2]*m2.mat[2][j]
        return ans

    def transpose(self, m2):
        ans=Matrix()
        for i in range(3):
            for j in range(3):
                ans.mat[i][j] = self.mat[j][i]
        return ans
    
    def display(self):
        for i in range(3):
            for j in range(3):
                print(self.mat[i][j],end=' ')
            print("\n")

print("Additon")
print()
m1=Matrix([[1,2,3],[4,5,6],[7,8,9]])
m2=Matrix([[9,8,7],[6,5,4],[3,2,1]])
m3=m1+m2
m3.display()

print("Multiplication")
print()
m4=m1 * m2
m4.display()

print("Transpose")
print()
m4=m1.transpose(m2)
m4.display()

#Q-3
import math

class Solid:
    def __init__(self):
        self.shape = ""
        self.dimensions = {}

    def accept_data(self):
        print("Choose the solid shape:")
        print("1. Cube")
        print("2. Sphere")
        print("3. Cylinder")
        choice = int(input("Enter your choice (1/2/3): "))

        if choice == 1:
            self.shape = "cube"
            side = float(input("Enter the side of the cube: "))
            self.dimensions['side'] = side

        elif choice == 2:
            self.shape = "sphere"
            radius = float(input("Enter the radius of the sphere: "))
            self.dimensions['radius'] = radius

        elif choice == 3:
            self.shape = "cylinder"
            radius = float(input("Enter the radius of the cylinder: "))
            height = float(input("Enter the height of the cylinder: "))
            self.dimensions['radius'] = radius
            self.dimensions['height'] = height

        else:
            print("Invalid choice.")
    
    def surface_area(self):
        if self.shape == "cube":
            side = self.dimensions['side']
            return 6 * side * side

        elif self.shape == "sphere":
            r = self.dimensions['radius']
            return 4 * math.pi * r * r

        elif self.shape == "cylinder":
            r = self.dimensions['radius']
            h = self.dimensions['height']
            return 2 * math.pi * r * (r + h)

        else:
            return 0

    def volume(self):
        if self.shape == "cube":
            side = self.dimensions['side']
            return side ** 3

        elif self.shape == "sphere":
            r = self.dimensions['radius']
            return (4/3) * math.pi * r ** 3

        elif self.shape == "cylinder":
            r = self.dimensions['radius']
            h = self.dimensions['height']
            return math.pi * r ** 2 * h

        else:
            return 0

solid = Solid()
solid.accept_data()

print("\nShape:", solid.shape.capitalize())
print("Surface Area:", round(solid.surface_area(), 2))
print("Volume:", round(solid.volume(), 2))

#Q-4
import math

class RegularShape:
    def __init__(self):
        self.shape = ""
        self.dimensions = {}

    def accept_data(self):
        print("Choose a regular shape:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Triangle (Equilateral)")
        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            self.shape = "square"
            side = float(input("Enter the side of the square: "))
            self.dimensions['side'] = side

        elif choice == 2:
            self.shape = "rectangle"
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            self.dimensions['length'] = length
            self.dimensions['width'] = width

        elif choice == 3:
            self.shape = "circle"
            radius = float(input("Enter the radius of the circle: "))
            self.dimensions['radius'] = radius

        elif choice == 4:
            self.shape = "triangle"
            side = float(input("Enter the side of the equilateral triangle: "))
            self.dimensions['side'] = side

        else:
            print("Invalid choice.")

    def area(self):
        if self.shape == "square":
            s = self.dimensions['side']
            return s * s

        elif self.shape == "rectangle":
            l = self.dimensions['length']
            w = self.dimensions['width']
            return l * w

        elif self.shape == "circle":
            r = self.dimensions['radius']
            return math.pi * r * r

        elif self.shape == "triangle":
            s = self.dimensions['side']
            return (math.sqrt(3) / 4) * s * s

        else:
            return 0

    def perimeter(self):
        if self.shape == "square":
            s = self.dimensions['side']
            return 4 * s

        elif self.shape == "rectangle":
            l = self.dimensions['length']
            w = self.dimensions['width']
            return 2 * (l + w)

        elif self.shape == "circle":
            r = self.dimensions['radius']
            return 2 * math.pi * r

        elif self.shape == "triangle":
            s = self.dimensions['side']
            return 3 * s

        else:
            return 0

shape = RegularShape()
shape.accept_data()

print("\nShape:", shape.shape.capitalize())
print("Area:", round(shape.area(), 2))
print("Perimeter/Circumference:", round(shape.perimeter(), 2))

#Q-5
class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize()

    def normalize(self):
        self.minutes += self.seconds // 60
        self.seconds %= 60
        self.hours += self.minutes // 60
        self.minutes %= 60

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def __add__(self, other):
        new_hours = self.hours + other.hours
        new_minutes = self.minutes + other.minutes
        new_seconds = self.seconds + other.seconds
        return Time(new_hours, new_minutes, new_seconds)

    def __sub__(self, other):
        total_self = self.to_seconds()
        total_other = other.to_seconds()
        total_diff = abs(total_self - total_other)
        return Time.from_seconds(total_diff)

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def from_seconds(seconds):
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return Time(hours, minutes, seconds)

time1 = Time(2, 45, 50)
time2 = Time(1, 20, 30)

print("Time 1:", time1)
print("Time 2:", time2)

sum_time = time1 + time2
print("Time 1 + Time 2:", sum_time)

diff_time = time1 - time2
print("Time 1 - Time 2:", diff_time)

print("Time 1 in seconds:", time1.to_seconds())
print("Time 2 in seconds:", time2.to_seconds())

#Q-6
class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]  

    def __str__(self):
        return f"{self.date[0]:02}-{self.date[1]:02}-{self.date[2]}"

    def __eq__(self, other):
        return self.date == other.date

date1 = Date(22, 4, 2025)
date2 = Date(22, 4, 2025)
date3 = Date(23, 4, 2025)

print("Date 1:", date1)
print("Date 2:", date2)
print("Date 3:", date3)

print("\nIs Date 1 equal to Date 2?", date1 == date2)
print("Is Date 1 equal to Date 3?", date1 == date3)

#Q-7
class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

    def __str__(self):
        return f"Weather Parameters: {', '.join(self.parameters)}"

today_weather = Weather(["Sunny", "Windy", "Dry"])

print(today_weather)

print("\nIs it Sunny today?", "Sunny" in today_weather)
print("Is it Rainy today?", "Rainy" in today_weather)

#Q-8
class MyString:
    def __init__(self, text):
        self.text = text

    
    def __str__(self):
        return self.text

    
    def __iadd__(self, other):
        if isinstance(other, MyString):
            self.text += other.text
        elif isinstance(other, str):
            self.text += other
        return self

    
    def toLower(self):
        self.text = self.text.lower()

    
    def toUpper(self):
        self.text = self.text.upper()


s1 = MyString("Hello")
s2 = MyString(" World")

print("Original Strings:")
print("s1:", s1)
print("s2:", s2)


s1 += s2
print("\nAfter s1 += s2:")
print("s1:", s1)

s1.toUpper()
print("\nAfter toUpper:")
print("s1:", s1)


s1.toLower()
print("\nAfter toLower:")
print("s1:", s1)
                

                
                

