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


