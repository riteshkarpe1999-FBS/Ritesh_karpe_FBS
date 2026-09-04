

# Easy program to calculate painting cost

area = float(input("Enter area of one wall: "))
cost_interior = float(input("Enter cost per unit area for interior wall: "))
cost_exterior = float(input("Enter cost per unit area for exterior wall: "))
n_interior = int(input("Enter number of interior walls: "))
n_exterior = int(input("Enter number of exterior walls: "))

total_cost = (area * n_interior * cost_interior) + (area * n_exterior * cost_exterior)

print("Total painting cost =", total_cost)









