# dictionaries, use curly brackets and colons
empty_dictionary = {}
dct = {'key1':'value1', 'key2':'value2','key3':'value3'}
person = {
    'first_name': 'John',
    'last_name' : 'Smith',
    'age': 25,
    'country': 'United States of America',
    'is_married':True,
    'skills':['soccer', 'math', 'coding', 'philosophy'],
    'address':{
        'street': 'Van Nostrand',
        'zipcode': '02210'
    }
}

# Dictionary length
print(len(person)) # 7

# Accessing dictionary items
print(person['first_name'])
print(person['is_married'])
print(person['address'])
print(person['skills'])

# accessing an item by key name raises an error if the key doesn't exist
# get() method returns None, which is a NoneType object data type, if the key doesn't exist
stock = {
    'name':'Apple',
    'ticker':'AAPL',
    'p/e_ratio': 34.6,
    'sector': 'technology',
    'CEO':'Tim Cook',
    'is_worth_trillions': True
}

print(stock.get('name'))
print(stock.get('CEO'))
print(stock.get('sector'))
print(stock.get('valuation')) # None

# adding items to a dictionary
credentials = {
    'college': True,
    'convict': False,
    'job_experience':'5 years',
    'references':['Barry Allen', 'Hal Jordan', 'Clark Kent']
}
credentials['university'] = 'University of Pennsylvania'
credentials['references'].append('Bruce Wayne')
print(credentials)

# modifying items in a dictionary
student = {
    'GPA': 3.9,
    'grade':'sophomore',
    'teacher':'Mr. Munsey',
    'plays_sports':True
}
print(student)
# modifications
student['GPA'] = 3.4
student['grade'] = 'junior'
print(student)

# checking keys in a dictionary, use the 'in' operator
job = {
    'salary': 75000,
    'health_benefits': True,
    'company' : 'Hewlett-Packard',
    'in_person':True,
    'degree':'marketing'
}
print('company' in job) # True
print('employer' in job) # False

# removing key and value pairs from a dictionary
dinner = {
    'formal':False,
    'main_course':'beef sirloin',
    'Number of guests': 20,
    'chef_name':'Gorgon Ramsey',
    'restaurant':'Hell''s Kitchen',
    'dessert':'sticky toffee pudding'
}
dinner.pop('main_course') # removes the item with the specified key name
dinner.popitem() # removes the last item
del dinner['restaurant'] # removes an item with specified key name

# changing dictionary to a list of items
# items() method changes dictionary to a list of tuples
stock = {
    'name':'Apple',
    'ticker':'AAPL',
    'p/e_ratio': 34.6,
    'sector': 'technology',
    'CEO':'Tim Cook',
    'is_worth_trillions': True
}
print(stock.items()) # dict_items([('name', 'Apple'), ('ticker','AAPL')...])

# clearing a dictionary
team = {
    'stadium':'Camp Nou',
    'best_player':'Pessi',
    'is_Barcelona':True,
}
print(team.clear()) # None

# deleting a dictionary
player = {
    'left_footed': True,
    'position':'striker',
    'nationality':'Norway'
}
del player

# copy a dictionary
band = {
    'lead_singer':'Brandon Flowers',
    'alternative_rock':True,
    'best_song':'Mr. Brightside'
}
band_copy = band.copy() # make a copy of the dictionary to avoid mutation of original dictionary

# getting dictionary values as a list
# values() method gives all values of dictionary as a list
superhero = {
    'identity':'Bruce Wayne',
    'sidekick':'Robin',
    'city':'Gotham'
}
values = superhero.values()
print(values)

# exercise 1
dog = {}
print(dog)
dog = {
    'name':'rufus',
    'color':'brown',
    'legs': 4,
    'age': 5
}
print(len(dog))

student = {
    'first_name':'Sammy',
    'last_name':'LeBoeuf',
    'gender':'male',
    'age': 17,
    'marital_status':False,
    'skills':['math', 'english', 'science', 'coding'],
    'country':'France',
    'city':'Marseille',
    'address':{
        'street':'220 Croissant Avenue',
        'zipcode':6767
    }
}
print(student)
# check the length of the student dictionary
print(len(student))
# get the value of skills and check the data type (it should be a list)
skills_list = student['skills']
print(type(skills_list))
student['city']='Toulouse'
skills_list.extend(['sports', 'physics'])

# check keys in dictionary
print('marital_status' in student) # True

# get the dictionary values as a list
student_list = student.values()
print(student_list)

# change the dictionary to a list of tuples using items() method
print(student.items()) 

# get the keys as a list
student_keys_list = list(student.keys())
print(student_keys_list)
print(list(student))

# delete one of the items in a dictionary
del student['gender']
print(student)
# delete one of the dictionaries
del student
