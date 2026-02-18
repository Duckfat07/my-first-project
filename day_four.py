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
