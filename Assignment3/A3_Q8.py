
import random

# Predefined userid and password
USERID = "admin"
PASSWORD = "1234"

# Prompt user for credentials
userid = input("Enter userid: ")
password = input("Enter password: ")

if userid == USERID and password == PASSWORD:
    # Generate a random 4-digit number
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)
    
    # Ask user to re-enter the captcha
    user_input = int(input("Enter the captcha shown above: "))
    
    if user_input == captcha:
        print("✅ Login successful!")
    else:
        print("❌ Login failed! Incorrect captcha.")
else:
    print("❌ Invalid userid or password.")



























