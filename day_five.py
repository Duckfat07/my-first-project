empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # this will print 0 because there are no items in the list

# list of fruits
fruits = ['banana', 'apple', 'orange', 'mandarins', 'strawberries']
print(fruits) # this will print the list of fruits
print(len(fruits)) # this will print the number of items in the list, which is 5

# list of vegetables 
vegetables = ['green beans', 'lettuce', 'potatoes', 'carrots', 'celery'] 
print(vegetables)
print(len(vegetables))
print('vegetables:', vegetables)
print('number of vegetables:', len(vegetables))

# list of coding languages 
coding_languages = ['python', 'HTML', 'CSS', 'JavaScript']
print(coding_languages)
print(len(coding_languages))
print('coding languages:', coding_languages)
print('number of coding languages:', len(coding_languages))

# list of cities
cities = ['New York', 'Paris', 'London', 'Tokyo', 'Dubai', 'Beijing', 'Moscow']
print('Famous cities:',cities)
print('Number of of cities:', len(cities))

# Modifying list
best_foods = ['pasta', 'pizza', 'burger', 'sushi', 'burrito']
first_food = best_foods[0] # accessing the first item using its index
print('First food:', first_food)
second_food = best_foods[1] # accessing the second item using its index
print('Second food:', second_food)
# last index
last_index = len(best_foods) - 1 # calculating the last index by subtracting 1 from the length of the list
last_food = best_foods[last_index] # accessing the last item using the last index
print('last food:', last_food)

# accessing items
cheeses = ['cheddar', 'swiss', 'parmesan']
last_cheese = cheeses[-1] # accessing the last item using negative indexing
print('last cheese:', last_cheese)
second_last_cheese = cheeses[-2]
print('second last cheese:', second_last_cheese)


# slicing items
utensils = ['fork', 'spoon', 'knife']
all_utensils = utensils[0:3] # it returns all the fruits
print('all utensils:', all_utensils)
all_utensils = utensils[0:] # it returns all the fruits, just like the one above
fork_and_spoon = utensils[0:2] # it does not include the end index
print('fork and spoon:', fork_and_spoon)
fork_spoon_knife = utensils[-3:] # it returns all the items starting from the third last item to the end of the list, -1 is knife, -2 is spoon, -3 is fork
print('common utensils:', fork_spoon_knife)

utensils = ['fork', 'spoon', 'knife']
utensils[0] = 'spork' # modifying the first item in the list
print('modified utensils:', utensils)
utensils[1] = 'chopsticks' # modifying the second item in the list
print('modified utensils:', utensils)
last_index = len(utensils) -1
utensils[last_index] = 'spatula' # modifying the last item in the list
print('modified utensils:', utensils)

# checking items
tech = ['phone', 'laptop', 'smartwatch']
does_exist = 'phone' in tech # checking if 'phone' is in the list tech, it will return True
print('Does phone exist in tech?', does_exist)
does_exist = 'tablet' in tech # False

# append
instruments = ['violin', 'piano', 'guitar']
instruments.append('drums') # adding 'drums' to the end of the list
print('instruments:', instruments)
instruments.append('harpsichord') # adding 'harpsichord' to the end of the list
print('instruments:', instruments)
instruments.append('oboe') # adding 'oboe' to the end of the list
print('instruments:', instruments)

# insert
colors = ['red', 'blue', 'green']
colors.insert(0, 'purple') # insert 'purple at index 0, which is the beginning of the list
colors.insert(2, 'yellow') # insert 'yellow at index 2, which is between 'blue' and 'green'
colors.insert(5, 'orange') # insert 'orange at index 5, which is between 'green' and the end of the list
print('colors:', colors) 
colors.insert(9, 'pink') 
print('colors:', colors) # if the index is greater than the length of the list, it will add the item to the end of the list
colors.insert(-1, 'black') # insert 'black' at index -1, which is the last item in the list, it will add 'black' before 'pink' 
print('colors:', colors)

# remove
heroes = ['batman', 'superman','wonder woman', 'flash', 'aquaman', 'cyborg', 'green lantern', 'martian manhunter', 'hawkgirl', 'supergirl']
heroes.remove('superman') # removes superman from the list
print('heroes:', heroes)
heroes.remove('aquaman') # removes aquaman from the list
print('heroes:', heroes)

# pop 
popped_hero = heroes.pop() # removes the last item from the list and returns it 
print('popped hero:', popped_hero) # it will print 'flash' because it was the last item in the list
print('heroes:', heroes) # it will print the list of heroes after popping 'flash'
heroes.pop(2) # removes the item at index 2, which is 'wonder woman' 
print('heroes:', heroes) 

# del
del heroes[0] # deletes the item at index 0, which is 'batman'
print('heroes:', heroes) # it will print the list of heroes after deleting 'batman' 
del heroes[1:3] # deletes the items from index 1 to index 2, which are 'cyborg' and 'green lantern' 
del heroes[-1] # deletes the last item in the list, which is 'supergirl'
print(heroes) # it will print the list of heroes after deleting 'cyborg' and 'green lantern' 
del heroes # deletes the entire list of heroes


# clear 
appliances = ['fridge', 'oven', 'microwave', 'dishwasher']
appliances.clear() # this will remove all the items from the list
appliances.append('toaster') # adds toaster to the list
print(appliances) # it will print ['toaster'] because the list was cleared before and then 'toaster' was added to the list 

# copying a list
organs = ['heart', 'liver', 'kidneys', 'lungs']
organs_copy = organs.copy() # this will create a copy of the list organs and assign it to organs_copy
print(organs_copy) # it will print the copied list of organs
organs_copy.append('brain') # this will add 'brain' to the copied list of organs
print(organs_copy) # it will print the copied list of organs with 'brain'

# joining lists
positive_words = ['happy', 'joyful', 'excited']
neutral_words = ['okay', 'fine', 'average']
negative_words = ['sad', 'angry', 'depressed']
descriptive_adjectives = positive_words + neutral_words + negative_words # this will join the three lists together
print(descriptive_adjectives)
bright_colors = ['red', 'yellow', 'orange']
dark_colors = ['black', 'navy', 'gray']
all_colors = bright_colors + dark_colors 
print(all_colors)

# join with extend
fruits = ['apple', 'plum', 'peach']
peeled_fruits = ['banana', 'orange', 'grapefruit']
fruits.extend(peeled_fruits) # this will add the items from peeled_fruits
print(fruits) # it will print the list of fruits with the added items
bright_colors.extend(dark_colors)
print(bright_colors) # it will print the list of bright colors with the added dark colors


# count
names = ['john', 'jane', 'john', 'jack', 'jill', 'john']
print(names.count('john')) # this will print 3 because there are three occurrences
ages = [25, 30, 25, 24, 22, 23, 20, 20, 21, 23, 23, 25, 25]
ages.count(25) == 4
print(ages.count(25)) # this will print 4 because there are four occurrences of 25 in the list

# index
ages = [25, 30, 25, 24, 22, 23, 20, 20, 21, 23, 23, 25, 25]
print(ages.index(24)) # this will print 3 because the first occurrence of 24 is at index 3 in the list of ages
fruits = ['apple', 'plum', 'peach', 'banana', 'orange', 'grapefruit']
print(fruits.index('banana')) # this will print 3 because 'banana' is at index 3 in the list of fruits
print(fruits.index('grapefruit')) # this will print 5 because 'grapefruit' is at index 5 in the list of fruits

# Reverse
colors = ['red', 'blue', 'green', 'yellow']
colors.reverse() # this will reverse the order of the items in the list
print(colors) # it will print the reversed list of colors

# sort
materials = ['wood', 'metal', 'plastic', 'glass']
materials.sort() # this will sort the list in alphabetical order
print(materials) # it will print the sorted list of materials
materials.sort(reverse=True) # this will sort the list in reverse alphabetical order
print(materials) # it will print the sorted list of materials in reverse alphabetical order
numbers = [2, 6, 3, 10, 50, 44, 39, 90, 2, 32]
numbers.sort() # this will sort the list of numbers in ascending order
print(numbers) # it will print the sorted list of numbers
numbers.sort(reverse=True) # this will sort the list of numbers in descending order
print(numbers) # it will print the sorted list of numbers in descending order