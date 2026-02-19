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

# Escape sequence
print('I hope everyone is enjoying the Python competition. \nDo you') # \n is a new line character, it moves the text after it to a new line
print('Days\tTopics\tExercises') #\t is a tab character, it adds a horizontal space between the words
print('Day1\t3\t5') # \t is a tab character, it adds a horizontal space between the words
print('Day 2\t3\t5') # printing the same thing with different spacing to show the effect of \t 
print('This is a backslash symbol (\\)') # to print a backslash we need to escape it with another backslash, so we use \\
print('In every programming language it starts with \"Hello, World!\"')

# String Methods
# capitalize(): converts the first character of the string to a capital letter
challenge = 'thirty days of python'
print(challenge.capitalize()) # Thirty days of python

# count(): returns the number of times a specific character or substring appears in the string
print(challenge.count('y')) # 3, counts the number of times 'y' appears in the string
# string.count(value, start,end) - counts the number of times a specific character or substring appears in the string from the start index to the end index (not including the end index)
print(challenge.count('y', 7, 15)) # 2, counts the number of times 'y' appears in the string from index 7 to 15

# endswith(): checks if a string ends with a specified ending
challenge = 'thirty days of python'
print(challenge.endswith('on')) # True, checks if the string ends with 'on'
print(challenge.endswith('tion')) # False, checks if the string ends with 'tion'

# expandtabs(): replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs()) # thirty   days    of      python, replaces each tab character with 8 spaces
print(challenge.expandtabs(4)) # thirty   days    of  python, replaces each tab character with 4 spaces

# find(): returns the index of first occurrence of substring
challenge = 'thirty days of python'
print(challenge.find('y')) # 5 - returns the index of the first occurrence of 'y' in the string
print(challenge.find('th')) # 0 - returns the index of the first occurrence of 'th' in the string

# format(): formats string into nicer output
first_name = 'John'
last_name = 'Doe' 
job = 'technician'
country = 'Serbia'

sentence = 'I am {} {}. I am a {}. I live in {}.'.format(
    first_name, last_name, job, country)
print(sentence) # I am John Doe. I am a technician. I live in Serbia. 

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}.'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314.0.

# index(): returns the index of substring, but raises an error if the substring is not found
challenge = 'thirty days of python'
print(challenge.index('i')) # 2 - returns the index of the first occurrence of 'i' in the string
print(challenge.index('th')) # 0 

#isalnum(): checks if all characters in the string are alphanumeric (letters and numbers)
challenge = 'thirtydays0fpython'
print(challenge.isalnum()) # True, all characters in the string are alphanumeric
challenge  = '30DaysOfPython'
print(challenge.isalnum()) # True, all characters in the string are alphanumeric, .isalnum() does not take any arguments, it only checks if all characters in the string are alphanumeric
challenge = 'thirtt days of python'
print(challenge.isalnum()) # False, there are space characters in the string, which are not alphanumeric
challenge = 'thirty_days_of_python'
print(challenge.isalnum()) # False, there are underscore characters in the string, which are not alphanumeric

# isalpha(): checks if all characters are alphabetic (letters)
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, there are space characters in the string
challenge = 'thritydaysofpython'
print(challenge.isalpha()) # True, because all characters in the string are letters
challenge = 'thirty_days_of_python'
print(challenge.isalpha()) # False, underscores are not letters

# isdecimal(): checks decimal characters (0-9), this method just checks if all characters in the string are decimal characters, which are base numbers 0-9. It does not take into account negative numbers, decimal points, or other characters that may be used in numeric representations.
challenge = '123'
print(challenge.isdecimal()) # True, all characters in the string are decimal characters
challenge = '12.3'
print(challenge.isdecimal()) # False, there is a dot character in the string, which is not a decimal character
num = '-123'
print(num.isdecimal()) # False

# isdigit(): checks digit characters (0-9), this method checks if all characters in the string are digit characters, which are base numbers 0-9. 
challenge = 'thirty'
print(challenge.isdigit()) # False
challenge = '123'
print(challenge.isdigit()) # True

# isidentifier(): checks if the string is a valid identifier, which means it can be used as a variable name in Python. A valid identifier must start with a letter (a-z or A-Z) or an underscore (_) and can be followed by letters, digits (0-9), or underscores. It cannot contain spaces or special characters. It can't start with a digit.
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a digit
challenge = '_thirty_days_of_python'
print(challenge.isidentifier()) # True, because it starts with an underscore and contains only letters

# islower(): checks if all alphabets in a string are lowercase

