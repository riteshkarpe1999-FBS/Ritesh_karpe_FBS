###Write a program to find the area and perimeter of following figure (Accept the
### length, breadth and radius from user                                        
import math

length = int(input("Enter length of rectangle: "))
breadth = int(input("Enter breadth of rectangle: "))
radius = int(input("Enter radius of semicircle: "))

# Area = rectangle area + semicircle area
area = (length * breadth) + (0.5 * math.pi * radius * radius)

perimeter = (2 * length + breadth) + (math.pi * radius)

# Output
print("Area of the figure =", area)
print("Perimeter of the figure =", perimeter)













