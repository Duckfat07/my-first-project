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

