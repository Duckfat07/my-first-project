# single line comment
letter = 'e'
print(letter)
print(len(letter))
greeting = 'Goodbye World!'
print(greeting)
print(len(greeting))

print(len(greeting) == 14) # True

sentence = 'The skinny python ate the fat cat.'
print(sentence)
print(sentence[0]) # prints 'T', the first character of a string
print(sentence[12] + sentence[13]) # prints 'py', the 13th and 14th characters of a string

# multi line string
paragraph = '''The astronaut flew to the moon and he looked down at the earth. 
He saw the blue oceans and the green land. 
He was amazed by the sheer scale of the earth and how small he felt in comparison. '''
print(paragraph)

# another way of doing the same thing
paragraph2 = """The astronaut flew to the moon and he looked down at the earth. 
He then traveled to Mars and he saw the red deserts and the towering mountains.
He watched interstellar by Christopher Nolan and was happy that his dream had become reality."""
print(paragraph2)

# String Concatenation 
first_name = 'Tom'
last_name = 'Brady'
space = ' '
full_name = first_name + space + last_name
print(full_name)

name = input('What is your first name?')
surname = input('What is your last name?')
official_name = name + space + surname
print('Your official name is ' + official_name)
# Checking length of a string using built-in len() function
print(len(first_name))
print(len(last_name + space + first_name))
print(len(full_name) == len(first_name + space + last_name))

# Unpacking characters
language = 'Python'
a, b, c, d, e, f = language
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

word = 'pie'
1, 2, 3 = word
print(1) # p
print(2) # i 
print(3) # e
print(1+2+3) # pie
print(word[0]) # p
print(word[1]) # i
print(word[2]) # e
print(word[0] + word[1] + word[2]) # pie 

# Accessing characters in strings by index
clothing = 'pants'
first_letter = clothing[0]
print(first_letter) # p
second_letter = clothing[1]
print(second_letter) # a
last_index = len(clothing) - 1
last_letter = clothing[last_index]
print(last_letter) # s 

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

# Slicing
language = 'Python'
# starts at zero index and up to 3 but not include 3
first_three = language[0:3]
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three) # hon
last_three = language[3:]
print(last_three) # hon

# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2]
print(pto) # Pto, 0(start):6(stop):2(step), prints every second character starting from index 0 up to but not including index 6



