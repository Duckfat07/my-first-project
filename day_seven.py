# sets
st = set()
st = {'item1', 'item2', 'item3'}

# use the len method to find the length of a set
fridge_brands = {'Samsung', 'Frigidaire', 'Wolf', 'Miele'}
print(len(fridge_brands))

st = set('rice', 'beans', 'tortilla')
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

# remove method
stocks = {'AAPL', 'NVDA', 'META'}
stocks.remove('META')
print(stocks)
print('Is META in the list of stocks', 'META' in stocks)
# pop method
colors = {'blue', 'red', 'black'}
removed_item = colors.pop()

st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
print(st)

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



 

