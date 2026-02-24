# syntax
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
