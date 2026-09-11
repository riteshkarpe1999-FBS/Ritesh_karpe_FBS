### WAP to print Armstrong number within a given range
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for num in range(start, end + 1):
    str_num = str(num)
    n = len(str_num)
    sum_of_powers = sum(int(digit) ** n for digit in str_num)
    if sum_of_powers == num:
        print(num)

 
    













