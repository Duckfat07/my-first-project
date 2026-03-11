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