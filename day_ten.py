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

