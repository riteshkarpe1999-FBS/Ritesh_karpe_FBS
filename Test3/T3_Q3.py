### Write a program to accept basic salary of n emp.
n = int(input("Enter number of employees: "))
total_all = 0

for i in range(1, n+1):
    basic = int(input(f"Enter basic salary of employee {i}: "))

    if basic < 20000:
        da = 0.10 * basic
        ta = 0.12 * basic
        hra = 0.15 * basic
    else:
        da = 0.15 * basic
        ta = 0.18 * basic
        hra = 0.20 * basic

    total = basic + da + ta + hra
    print("Total salary of employee", i, "=", total)
    total_all += total

print("Total salary of all employees =", total_all)









