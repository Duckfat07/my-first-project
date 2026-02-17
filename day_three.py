# Arithmetic Operations in Python
# Integers

print('Addition:', 4+5)
print('Subtraction:',6-5)
print('Multiplication:', 4*3)

# Division in python gives floating number
print('Division:', 6/3)
print('Division:', 3/2)
print('Division:', 8/3)
# gives without the floating number or without the remainder
print('Division without the remainder:', 67//5)
print('Modulus:', 5%2)                 # gives the remainder
print('Division woithout the remainder:', 7//2)
print('Exponential:', 5**3)          # # it means 5*5*5

# Floating numbers
print('Floating Number, Pi:', 3.14)
print('Floating Number, gravity:', 9.81)
print('Floating Number, body temperature in celsius:', 36.6)

# Complex Numbers
print('Complex number:', 2+3j)
print('Multiplying complex number:', (2+3j)*(2-3j))

# Declaring the variable at the top first

a = 3 # a is a variable and 3 is an integer data type
b = 5 # b is a variable and 5 is an integer data type

# Arthmetic operations and assigning the result to a variable
sum = a + b
total = a + b
diff = a - b
product = a * b
division = a / b
floor_division = a // b # this gives the quotient without the remainder
remainder = a % b
exponential = a ** b

print(total)
print('total:', total)
print('sum:',sum)
print('a + b:', sum)
print('a - b:', diff)
print('a * b:', product)
print('a / b:', division)
print('a % b:', remainder)
print('a // b:', floor_division) # returns the quotient without the remainder
print('a ** b:', exponential) # returns a to the power of b

# Declaring values and organizing them together
num_one = 5
num_two = 10

# Artithmetic operations
total = num_one + num_two
diff - num_two - num_one
div = num_two / num_one
product = num_one * num_two
remainder - num_two % num_one # only returns the remainder 
floor_division = num_two // num_one # returns the quotient of the division without the remainder
exponential = num_one ** num_two # returns the value of num_one to the power of num_two

# Printing values with label
print('Total:', total)
print('Difference:', diff)
print('Division:', div)
print('Product:', product)

# Calculating the area of a circle
pi = 3.141592653589793
radius = 15 # radius of a circle
# two * sign means exponent of power 
area_of_circle = pi * radius ** 2
print('Area of a circle:', area_of_circle)

# Calculating the area of a rectangle
l = 15 # length of a rectangle
w = 25 # width of a rectangle
area_of_rect = l*w
print('Area of a rectangle:', area_of_rect)

# Calculating the area of a triangle
b, h = 80, 40 # base and height of a triangle
area_of_triangle = 1/2 * b * h
print('Area of a triangle:', area_of_triangle)

# Calculating the area of a trapezoid
area_of_trap = 1/2*(b+h)*l
print('Area of a trapezoid:', area_of_trap)

# Calculating the volume of a sphere
volume_of_sphere = 4/3 * pi * radius ** 3
print('Volume of a sphere:', volume_of_sphere)

# Calculating the weight of an object
mass = int(input('Enter the mass of an object in kg:'))
gravity = 9.81 # gravity on earth (in m/s^2)
weight = mass * gravity
print('The weight of the object is:', weight, 'Newtons')

print(3 > 2) # True, because 3 is greater than 2
print(5 > 2) # false, because 2 is not greater than 5
print(3 == 3) # true, because 3 is equal to 3
print(3 != 4) # True, because 3 is not equal to 4
print(5 >= 4) # True, because 5 is greater than or equal to 4
print(3 != 2) # true because 3 is not equal to 2
print(len('fruit') == len('mango')) # True, because mango and fruit have the same number of characters
print(len('dog') != len('gazelle')) # True, because dog has 3 characters and gazelle has 7 characters
print(len('souffle') > len('pastry')) # True, because souffle has 7 characters and pastry has 6 characters
print(len('soccer') < len('basketball')) # True, because basketball has more characters
print(len('water') >= len('seltzer')) # False, because seltzer has more characters than water
print(len('father') <= len('son')) # False, because father has more characters than son

variable1 = "computer"
variable2 = "phone"

print(len(variable1) != len(variable2)) # True, because computer has more characters than phone

# Boolean comparison
print('True == True:', True == True) 
print('True == False:', True == False) # False, because True is not equal to False
print('False == False:', False == False) # True, because false is equal to false
print('True and True:', True and True) # True, because both conditions are true
print('True or False:', True or False) # True because at least one condition is true
print('False and False:', False and False) # False, because both conditions are false

# BOOLEAN COMPARISON & LOGICAL OPERATORS
# 
# Operands: The values on either side of an operator (in this case, True or False)
# 
# == (equality operator): Checks if two values are equal
#    Example: True == True returns True, True == False returns False
#
# and (logical AND): Returns True only if BOTH operands are True
#    Example: True and True returns True, True and False returns False
#
# or (logical OR): Returns True if AT LEAST ONE operand is True
#    Example: True or False returns True, False or False returns False

# Boolean comparison
print('True == True:', True == True) 
print('True == False:', True == False) # False, because True is not equal to False
print('False == False:', False == False) # True, because false is equal to false
print('True and True:', True and True) # True, because both conditions are true
print('True or False:', True or False) # True because at least one condition is true
print('False and False:', False and False) # False, because both conditions are false

# Another way comparison