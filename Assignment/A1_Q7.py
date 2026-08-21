### to Find the Roots of a Quadratic Equation

# take input
a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))


# perform operation
x = (b**2) - (4*a*c)
root1 = (-b - ((x)**0.5)) / (2*a)
root2 = (-b + ((x)**0.5)) / (2*a)

# display result
print('root',root1)
print('root',root2)










































