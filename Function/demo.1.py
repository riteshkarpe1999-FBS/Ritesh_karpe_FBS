#def greet():
 #   print('Good morning!')
#greet()



####   Addition


#addition()

####### type 2 
#def addition(num1, num2):
 #   sum = num1 + num2
  #  print("Sum:", sum)
#
#x = int(input("Enter first number1: "))
#y = int(input("Enter second number2: "))

#addition(x,y)



#type 3 ### without using peraameter
#def addition():
  #  num1 = int(input("Enter first number1: "))
  #  num2 = int(input("Enter second number2: "))

 #   sum = num1 + num2
#    return sum
#res = addition()
#print(res)

# type 4 ### using parameter and return value
#def addition(num1, num2):
   # sum = num1 + num2
   # return sum

#num1 = int(input("Enter first number1: "))
#num2 = int(input("Enter second number2: "))
#res = addition(num1, num2)
#print(res)



# Function to check prime number (Type 1: no parameters, no return value)

from typing import Type


def check_prime():
    num = int(input("Enter a number: ")) 
    
    if num > 1:
        for i in range(2, int(num**0.5) + 1): 
            if num % i == 0:
                print(num, "false")
                break
        else:
            print(num, "true ")
    else:
        print(num, "false")

# Call the function
check_prime()

### function to check pallindrome number (Type 1: no parameters, no return value)
def check_palindrome():
    num = int(input("Enter a number: "))
    original_num = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10

    if original_num == reversed_num:
        print(original_num, "true")
    else:
        print(original_num, "false")

### function to check strong (Type 1: no parameters, no return value )
def check_strong():
    num = int(input("Enter a number: "))
    original_num = num
    sum_of_factorials = 0

    while num > 0:
        digit = num % 10
        factorial = 1
        for i in range(1, digit + 1):
            factorial *= i
        sum_of_factorials += factorial
        num //= 10

    if original_num == sum_of_factorials:
        print(original_num, "true")
    else:
        print(original_num, "false")



### function to check armstrong number (Type 1: no parameters, no return value)
def check_armstrong():
    num = int(input("Enter a number: "))
    original_num = num
    sum_of_cubes = 0

    while num > 0:
        digit = num % 10
        sum_of_cubes += digit ** 3
        num //= 10

    if original_num == sum_of_cubes:
        print(original_num, "true")
    else:
        print(original_num, "false")


### function to check perfect number (Type 1: no parameters, no return value)
def check_perfect():
    num = int(input("Enter a number: "))
    original_num = num
    sum_of_divisors = 0

    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i

    if original_num == sum_of_divisors:
        print(original_num, "true")
    else:
        print(original_num, "false")


### Function to check prime number (Type 2: passing parameters, no return value)

def check_prime(num):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(num, "false")
                break
        else:
            print(num, "true ")
    else:
        print(num, "false")


### function to check pallindrome number (Type 2: passing parameters, no return value)

def check_palindrome(num):
    original_num = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10

    if original_num == reversed_num:
        print(original_num, "true")
    else:
        print(original_num, "false")

### function to check strong number (Type 2: passing parameters, no return value)

def check_strong(num):             
    original_num = num
    sum_of_factorials = 0

    while num > 0:
        digit = num % 10
        factorial = 1
        for i in range(1, digit + 1):
            factorial *= i
        sum_of_factorials += factorial
        num //= 10

    if original_num == sum_of_factorials:
        print(original_num, "true")
    else:
        print(original_num, "false")

### function to check armstrong number (Type 2: passing parameters, no return value)

def check_armstrong(num):
    original_num = num
    sum_of_cubes = 0

    while num > 0:
        digit = num % 10
        sum_of_cubes += digit ** 3
        num //= 10

    if original_num == sum_of_cubes:
        print(original_num, "true")
    else:
        print(original_num, "false")


### function to check perfect number (Type 2: passing parameters, no return value)

def check_perfect(num):
    original_num = num
    sum_of_divisors = 0

    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i

    if original_num == sum_of_divisors:
        print(original_num, "true")
    else:
        print(original_num, "false")



### function to check prime number (Type 3: no parameters, return value)

def check_prime_return():
    num = int(input("Enter a number: "))
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    else:
        return False



### function to check palindrome number (Type 3: no parameters, return value)

def check_palindrome_return():
    num = int(input("Enter a number: "))
    original_num = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10

    if original_num == reversed_num:
        return True
    else:
        return False




### function to check strong number (Type 3: no parameters, return value)


def check_strong_return():
    num = int(input("Enter a number: "))
    original_num = num
    sum_of_factorials = 0

    while num > 0:
        digit = num % 10
        factorial = 1
        for i in range(1, digit + 1):
            factorial *= i
        sum_of_factorials += factorial
        num //= 10

    if original_num == sum_of_factorials:
        return True
    else:
        return False


### function to check armstrong number (Type 3: no parameters, return value)


def check_armstrong_return():
    num = int(input("Enter a number: "))
    original_num = num
    sum_of_cubes = 0

    while num > 0:
        digit = num % 10
        sum_of_cubes += digit ** 3
        num //= 10

    if original_num == sum_of_cubes:
        return True
    else:
        return False




### function to check perfect number (Type 3: no parameters, return value)

def check_perfect_return():
    num = int(input("Enter a number: "))
    original_num = num
    sum_of_divisors = 0

    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i

    if original_num == sum_of_divisors:
        return True
    else:
        return False


### function to check prime number (Type 4: passing parameters, return value)

def check_prime_params(num):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    else:
        return False


### function to check palindrome number (Type 4: passing parameters, return value)


def check_palindrome_params(num):
    original_num = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10

    if original_num == reversed_num:
        return True
    else:
        return False



### function to check strong number (Type 4: passing parameters, return value)


def check_strong_params(num):
    original_num = num
    sum_of_factorials = 0

    while num > 0:
        digit = num % 10
        factorial = 1
        for i in range(1, digit + 1):
            factorial *= i
        sum_of_factorials += factorial
        num //= 10

    if original_num == sum_of_factorials:
        return True
    else:
        return False


### function to check armstrong number (Type 4: passing parameters, return value)


def check_armstrong_params(num):
    original_num = num
    sum_of_cubes = 0

    while num > 0:
        digit = num % 10
        sum_of_cubes += digit ** 3
        num //= 10

    if original_num == sum_of_cubes:
        return True
    else:
        return False




### function to check perfect number (Type 4: passing parameters, return value)

def check_perfect_params(num):
    original_num = num
    sum_of_divisors = 0

    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i

    if original_num == sum_of_divisors:
        return True
    else:
        return False



