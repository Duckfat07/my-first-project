# syntax - tuples are immutable (cannot be change)
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()
print(empty_tuple) # this will print an empty tuple
print(len(empty_tuple)) # this will print 0 because there are no items in the tuple

# syntax
tpl = ('item1', 'item2', 'item3')
fruits = ('banana', 'orange', 'apple')

# syntax with length of the tuple
tpl = ('item1', 'item2', 'item3')
print(tpl) 
print(len(tpl)) # 3

# accessing items in a tuple
fruits = ('banana', 'orange', 'lemon')
first_item = fruits[0] 
second_item = fruits[1]
last_index = len(fruits) - 1
last_item = fruits[last_index]
print(first_item, second_item, last_item)

# Negative indexing in tuples
tpl = ('item1', 'item2', 'item3')
first_item = tpl[-3]
second_item = tpl[-2]
last_item = tpl[-1]
print(first_item, second_item, last_item)

# slicing tuples - range of positive indexes
data = ('item1','item2','item3','item4','item5')
all_items = data[0:5] # all items
all_items = data[0:] # all items
print(all_items)
middle_three_items = data[1:4] # item2, item3, item4
print(middle_three_items)
first_three_items = data[:3] # item1, item2, item3
print(first_three_items)
last_three_items = data[2:] # item3, item4, item5
print(last_three_items)

# slicing tuples - range of negative indexes, data[start:stop] if start is empty, it defaults to 0
data = ('value1', 'value2', 'value3', 'value4')
all_items = data[-4:] # all items
print(all_items)
middle_two_values = data[-3:-1] # this will print value2 and value3 
print(middle_two_values)
first_two_values = data[:-2] # this will print value1 and value2 because it will start from the beginning of the tuple and end at index -2 (not including index -2)
print(first_two_values) 
value4 = data[-1] # this will print value4 because it is the last item in the tupleand we are using negative indexing to access it
print(value4)

# changing tuples to lists
tpl = ('item1','item2','item3')
# convert tuple to list
lst = list(tpl)
print(lst) # this will print the list version of the tuple
# changing the list
fruits = ('banana', 'orange', 'apple')
fruits = list(fruits) # convert tuple to list
fruits[0] = 'mango' # changes the first item in the list to 'mango'
fruits[1] = 'lemon' # changes the second item in the list
fruits[2] = 'strawberry' # changes the third item in the list to 'strawberry'
print(fruits) # this will print the modified list

# checking an item in a tuple
tpl = ('item1', 'item2', 'item3')
'item2' in tpl # True, because 'item2' is in the tuple
print('item2' in tpl) # this will print True

colors = ('red', 'green', 'blue')
print('red' in colors) # this will print True
print('black' in colors) # this will print False

# Joining Tuples
tpl1 = ('one', 'two', 'three')
tpl2 = ('four', 'five', 'six')
joined_tuple = tpl1 + tpl2 # this will join the two tuples together
print(joined_tuple) # this will print the joined tuple

foods = ('pasta', 'burger', 'sushi')
desserts = ('brownie', 'pudding', 'cake')
foods_and_desserts = foods + desserts # this will join the two tuples together
print(foods_and_desserts) # this will print the joined tuple

# Deleting a tuple
tuple1 = ('joe', 'john', 'jane')
del tuple1 # this will delete the tuple
# print(tuple1) # this will raise an error because the tuple has been deleted
citrus = ('lemon', 'orange', 'grapefruit')
# del citrus[0] # this will raise an error because tuples are immutable and we cannot change them
del citrus # this will delete the tuple
# print(citrus) # this will raise an error because the tuple has been deleted

# Exercise 1
brothers = ('jim', 'jack', 'john')
sisters = ('jane', 'jill', 'jessica')
siblings = brothers + sisters 
print(siblings) 
print(len(siblings)) 
parents = ('michael', 'susan')
# join tuples
family_members = siblings + parents
print(family_members) 

# Exercise 2
# Unpacking a tuple 
a, b, *others = family_members
print(a, b, *others) # this will print the first two items in the tuple and the rest of the items will be stored in the 'others' variable as a list

# tuple methods
fruits = ('apple', 'blueberry','lime')
vegetables = ('lettuce', 'broccoli', 'spinach')
animal_products = ('beef', 'eggs', 'milk')
# Join
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp) # convert tuple to list
print(food_stuff_lt)
# slicing
middle_item = food_stuff_lt[4] 
print(middle_item) # this will print the middle item
first_three_items = food_stuff_lt[0:3] 
last_three_items = food_stuff_lt[-3:] 
print('first three items:', first_three_items)
print('last three items:', last_three_items)
del food_stuff_tp 

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries) 

food_stuff_lt.sort()
print(food_stuff_lt)
