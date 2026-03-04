# conditional statements
# equals: a == b
# not equals: a != b
# less than: a < b
# greater than: a > b
# less than or equal to: a <= b
# greater than or equal to: a >= b

# syntax for if statement
# if condition:
    # this part of the code runs for truthy conditions
a = 3
if a > 0:
    print('A is a positive number') # A is a positive number

# syntax for if-else statement
# if condition:
    # this part of code runs for truthy conditions
# else:
    # this part of code runs for false conditions
number = 30
if number > 30:
    print('the number is greater than 30')
else: 
    print('the number is less than or equal to 30') 
# else statement prints 'the number is less than or equal to 30'

# syntax for if-elif-else
# if condition:
    # code
# elif condition:
    # code
# else:
    # code
variable = -1
if variable > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else: 
    print('A is zero')
# the elif statement is true, so it will print

# short hand 
# syntax
# code if condition else code
b = 6
print('B is the number 6') if b == 6 else print('B is not the number 6')
# first condition is met, so 'B is number 6' will print

# Nested Conditions, if statements within an if statement 
# if condition:
#   code
#   if condition:
#       code
number = 0
if number > 0:
    if number % 2 == 0:
        print('number is a positive and even integer')
    else:
        print('number is just positive')
elif number == 0:
    print('number is zero')
else: 
    print('number is a negative number')

# we can avoid writing nested condition by using the logical operator 'and'
# syntax for if condition and logical operators 
# if condition and condition:
#   code
c = 10
if c > 0 and c % 2 == 0:
    print('C is an even and positive integer')
elif c > 0 and c % 2 != 0:
    print('c is a positive integer')
elif c == 0 :
    print('c is zero')
elif c != 11:
    print('c is not equal to 11')
else: 
    print('c is negative number')

# if and or logical operators
# syntax
# if condition or condition:
#   code
user = 'Teddy'
password = 3065
if user == 'admin' or password == 3065:
    print('Access Granted ')
else: 
    print('Access denied!')

string = ('I love hamburgers')
if 'hamburgers' in string:
    print('TRUE')
else: 
    print('false')

# logical operators
# and - if both conditions are true, returns true
# or - if one condition is true, returns true
# not - reverses the result, returns False if the result is true

# testing if a is NOT greater than b 
a = 5
b = 8
if not a > b:
    print('a is greater than b')
else: 
    print('a is not greater than b')

temp = 60 
is_raining = False
if temp >= 60 and not is_raining: 
    print('great day to be outside')

# Exercise 1
age = int(input('Enter your age:'))
if age >= 18:
    print('You are old enough to drive')
else:
    print('You need', 18 - age, 'more years to learn to drive')

my_age = 34
your_age = int(input('Enter your age:'))
if your_age >= my_age:
    print('You are', your_age - 34, 'years older than me')
else:
    print('I am', 34 - your_age, 'years older than you')

num1 = int(input('Enter number one:'))
num2 = int(input('Enter number two:'))
if num1 > num2:
    print(num1, 'is greater than', num2)
elif num2 > num1:
    print(num2, 'is greater than', num1)
elif num1 == num2:
    print(num1, 'is equal to', num2)
else:
    print('Not a number!!')