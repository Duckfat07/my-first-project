import math

num = int(input("Enter a number to calculate its factorial: "))

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The facorial of 0 is 1")
else:
    result = math.factorial(num)
    print(f"The factorial of {num} is {result}")