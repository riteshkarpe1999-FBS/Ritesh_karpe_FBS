
# Program to calculate total ticket amount with discounts

# Input: number of passengers
num_passengers = int(input("Enter number of passengers: "))

# Input: ticket price per person
ticket_price = float(input("Enter ticket price per person: "))

total_amount = 0

# Loop through each passenger
for i in range(1, num_passengers + 1):
    age = int(input(f"Enter age of passenger {i}: "))
    
    if age < 12:
        # Children below 12 get 30% discount
        amount = ticket_price * 0.7
    elif age > 59:
        # Senior citizens above 59 get 50% discount
        amount = ticket_price * 0.5
    else:
        # Others pay full price
        amount = ticket_price
    
    total_amount += amount

print("Total ticket amount for all passengers:", total_amount)






