
# Program to check if user has entered correct userid and password

# Predefined correct credentials
correct_userid = "admin"
correct_password = "12345"

# Taking input from user
userid = input("Enter User ID: ")
password = input("Enter Password: ")

# Checking credentials
if userid == correct_userid and password == correct_password:
    print("Login Successful!")
else:
    print("Invalid User ID or Password.")


















