# Program to check if a triangle is valid based on its angles

# Input angles
angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))
angle3 = float(input("Enter third angle: "))

# Check validity
if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3 == 180):
    print("The triangle is valid.")
else:
    print("The triangle is NOT valid.")

























