# Program to calculate total bill with GST

p1 = int(input("Enter price of product 1: "))
p2 = int(input("Enter price of product 2: "))
p3 = int(input("Enter price of product 3: "))
p4 = int(input("Enter price of product 4: "))
p5 = int(input("Enter price of product 5: "))


total = p1 + p2 + p3 + p4 + p5

# Add 18% gst
gst = total * 0.18
final_bill = total + gst

print("Total bill after adding 18% GST =", final_bill)






