# sets
st = set()
st = {'item1', 'item2', 'item3'}

# use the len method to find the length of a set
fridge_brands = {'Samsung', 'Frigidaire', 'Wolf', 'Miele'}
print(len(fridge_brands))

st = set(['rice', 'beans', 'tortilla'])
print('Does the set st contain rice?', 'rice' in st)

# add one item using add()
st = {'Radiohead', 'Red Hot Chili Peppers', 'Oasis'}
st.add('The Killers')
print(st)

# to add multiple items, use the update() method
school_supplies = {'pencil', 'pen', 'eraser', 'marker'}
school_supplies.update('lead', 'notebook', 'binder')
print(school_supplies)
print(len(school_supplies))

fruits = {'lime', 'apple', 'tomato'}
vegetables = {'onion', 'okra', 'shishito peppers'}
fruits.update(vegetables)
print(fruits)
print(len(fruits))

# remove method, this does raise an error if the item is missing in the set
stocks = {'AAPL', 'NVDA', 'META'}
stocks.remove('META')
print(stocks)
print('Is META in the list of stocks', 'META' in stocks)
# pop method
colors = {'blue', 'red', 'black'}
removed_item = colors.pop()
# discard() method, which does not return an error if the item does not exist in the set
stocks.discard('AAPL')
print(stocks)

# clearing items in a set
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
print(st)

# deleting a set
colleges = {'upenn', 'uva', 'cornell', 'princeton'}
del colleges

# converting list to set, removes duplicates and only unique items will be reserved
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst) #{'item2', 'item4', 'item1', 'item3'}
print(st)

# joining sets, use union(), update(), or | symbol
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'potato', 'onion', 'cabbage', 'cucumber'}
print(fruits.union(vegetables))
print(fruits | vegetables)
print(fruits.update(vegetables))

# intersection, use .intersection() or & symbol
fruits1 = {'pineapple', 'strawberry', 'blueberry', 'banana', 'orange', 'mandarin'}
fruits2 = {'apple', 'berry', 'orange', 'mandarin', 'pineapple'}
print(fruits1.intersection(fruits2))
print(fruits1 & fruits2)
whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
even_numbers = {0,2,4,6,8,10}
print(whole_numbers.intersection(even_numbers)) 

# checking subset and super set
# subset: issubset()
# super set: issuperset()
cool_sports = {'soccer', 'basketball', 'football', 'hockey'}
sports = {'soccer', 'hockey'}
print(cool_sports.issuperset(sports)) # True
print(sports.issubset(cool_sports)) # True
whole_numbers = {1,2,3,4,5,6,7,8,9,10}
even_numbers = {2,4,6,8,10}
print(whole_numbers.issuperset(even_numbers)) # True
print(even_numbers.issubset(whole_numbers)) # True

# checking the difference between two sets, returns the difference between two sets or using the - symbol
whole_numbers = {1,2,3,4,5,6,7,8,9,10}
even_numbers = {2,4,6,8,10}
whole_numbers.difference(even_numbers)
even_numbers.difference(whole_numbers)
print(whole_numbers.difference(even_numbers))
print(even_numbers.difference(whole_numbers))
print(whole_numbers - even_numbers)
print(even_numbers - whole_numbers)

# finding symmetric difference between two sets
# returns the symeetric difference, which means that it returns a set that contains all items from both sets, except items that are present in both sets, mathematically
# (A\B)U(B\A)
print(whole_numbers.symmetric_difference(even_numbers))
python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.symmetric_difference(dragon))

# Disjoint sets. If two sets do not have a common item, they are disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method
even_numbers = {0,2,4,6,8,10}
odd_numbers = {1,3,5,7,9}
odd_numbers.isdisjoint(even_numbers)
print(odd_numbers.isdisjoint(even_numbers)) # True

# Exercise 1
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# find length of the set it_companies
print(len(it_companies)) 
it_companies.add('Twitter')
it_companies.update('Amazon', 'TSMC', 'Broadcom', 'Samsung')
print(it_companies)
it_companies.remove('IBM')
print('Is IBM still relevant?', 'IBM' in it_companies)

# join A and B 
print(A | B)
print(A.union(B))
print(A.intersection(B))
# subset
print(A.issubset(B))
# Are A and B disjoint?
print(A.isdisjoint(B))
# Join A with B and B with A
print(A.update(B))
print(B.union(A))
# symmetric difference
print(A.symmetric_difference(B))
# delete sets
del A, B

# Exercise 3
age_set = set(age)
print(len(age_set))
print('Are the lengths of the set and the list of ages equal?',len(age_set) == len(age))

# difference between string, list, tuple, and set (they are all built-in data structures)
# string is immutable (unchangeable), ordered (indexed), allows duplicates
# list is mutable (changeable), ordered (indexes), allows duplicates
# tuple is immutable (unchangeable), ordered (indexed), allows duplicates
# set is mutable (add/remove elements), unordered (no indexing), does not allow duplicates (unique elements only)
# string 'hello' or "hello"
# list: [1,2,3]
# tuple: (1,2,3)
# set = {1,2,3}

string = "I am a teacher and I love to inspire and teach people"



 

