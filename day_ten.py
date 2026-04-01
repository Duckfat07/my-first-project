# LOOPS
# syntax
# while condition
#   code goes here

count = 0 
while count < 5:
    print(count)
    count = count + 1
# prints from 0 to 4

# while loop
# while condition 
#   code goes here
# else:
#   code goes here

count = 0
while count < 5: 
    print(count)
    count = count + 1
else:
    print(count)

# break and continue
# break: we use break when we like to get out of or stop the loop
# syntax
# while condition
#   code goes here
#   if another_condition:
#       break
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
# the above while loop only prints 0, 1, 2 but when it reaches 3 it stops

# continue: continue statement allows us to skip the current iteration, and continue with the next
# syntax
# while condition:
#   code goes here
#   if another_condition:
#       continue
number = 0 
while number < 5:
    if number == 3:
        count += 1 
        continue 
    print(count)
    count = count + 1
# the above while loop only prints 0, 1, 2, and 4 (skips 3)

# for loops 
# syntax - using For loop on list
# for iterator in lst:
#   code goes here

# example
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number) # the numbers will be printed line by line, from 0 to 5

# using For loop on string
# for iterator in string:
#   code goes here
language = 'Python'
for letter in language: 
    print(letter)

for i in range(len(language)):
    print(language[i])

# Using For loop on tuple
# for iterator in tpl:
#   code goes here
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
# For loop with dictionary 
# for iterator in dct:
#   code goes here
soccer_player = {
    'first_name':'Michael',
    'last_name':'Parks',
    'age': 85,
    'country':'Estonia',
    'is_married': True,
    'skills':['crossing','shooting','dribbling'],
    'address':{
        'street':'Van Nostrand',
        'zipcode':'07650'
    }
}
for key in soccer_player:
    print(key)
for key, value in soccer_player.items():
    print(key, value) # this way we get both keys and values printed out
# example output: first_name Michael

# Using For loop in set
# for iterator in st:
#   code goes here
# Example
infotech_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in infotech_companies:
    print(company)

# break and continue part 2 
# we use break when we want to stop our loop before it is completed
# for iterator in sequence:
#   code goes here
#   if condition:
#       break
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
# the loop stops when it reaches 3

# Continue: we use continue when we want to skip some of the steps in the iteration of the loop
# for iterator in sequence:
#   code goes here
#   if condition:
#       continue
numeros = (10,11,12,13,14,15)
for numero in numeros:
    print(numero)
    if numero == 13:
        continue
    print('Next numero should be ', numero + 1) if numero != 5 else print('outside the loop')
# if the number equals 13, the step after the condition (but inside the loop) is skipped and the execution of the loop continues if there are any iterations left

# The range function
# The range() function is used to return a list of numbers. The range(start, end, step) takes three parameters: starting, ending, and increment. By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end). Creating sequences using range
lst = list(range(11)) 
print(lst) # prints numbers from 0 to 10
st = set(range(1, 11)) # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # prints numbers from 1 to 10 

lst = list(range(0, 11, 3)) # 3 arguments indicate start, end, and step of the sequence
print(lst) # prints 0,3,6,9 
st = set(range(1, 11, 2)) 
print(st) # {1, 3, 5, 7, 9}

# for backward from start to end
lst = list(range(11, 0, -1)) 
print(lst) # [11, 9, 7, 5, 3, 1]

# syntax
# for iterator in range(start, end, step):

# for number in range(11):
#     print(number) # prints from 0 to 10, not including 11


# Nested For Loop
# syntax
# for x in y:
#     for t in x:
#         code goes here

person = {
    'name':'johnny',
    'age':25,
    'hobbies':['hiking', 'cooking', 'soccer'],
    'is_married': False,
    'address':{
        'avenue':'Columbus',
        'zipcode':'11111'
    }
}
for key in person:
    if key == 'hobbies':
        for hobby in person[key]:
            print(hobby) # prints hobbies one by one

# For Else
