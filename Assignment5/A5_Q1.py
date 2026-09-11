# Easy login check with 3 attempts

correct_userid = "vihaan"
correct_password = "0001"

for attempt in range(3):
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_userid and password == correct_password:
        print("Login Successful ")
        break
    else:
        print("Invalid credentials ")
else:
    print("Too many failed attempts. Program terminated ")











