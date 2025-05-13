###################### Primitive Types ###########################

############# VARIABLES ############
# Make sure that variable names are specific
# User lower case when naming variables
# Use and underscore when seperating words
# Put a space between the equals sign and the variable

import math
students_count = 1000  # Integer
rating = 4.9  # Float
is_published = False  # Boolean - either true or false
course_name = "Python Programming"  # String
print(students_count)

########### STRINGS ############

course = "Python Programming"
print(len(course))  # Prints the length of the course variable
print(course[0])  # Prints the character at position 0 of the course variable
print(course[-1])  # Prints the last character of the course variable
print(course[0:3])  # Prints the first 3 characters of the course variable
# If an end index isn't included then everything after the starting index will be included
# If a beginning index isn't included then 0 is put in my default
# If we don't included a start or end index then it will print then entire variable
# The argument of [0:3] will start at the beginning of the string and print everything up to
# but NOT including the 3rd index since we start at 0 - >Pyt


############### Escape Sequences ################
# \"" - Adds a double quote to the code
# \' - Adds a single quote to the code
# \\ - Adds a backslash to the the code
# \n - Prints a new line

course1 = "Python \"Programming"
print(course1)


################## Formatted Strings ###################
# When using formatted strings you can put any expression between the curly bracese and the values will be replaced at runtime

first = "Brantley"
last = "Cragun"

# Concatination method, can be done but using a formatted string would be more effective here
full1 = first + " " + last
print(full1)

# Defines a variable called full and uses a formatted string to print the first and last name using curly braces
full = f"{first} {last}"
print(full)


################### String Methods #######################
# String methods return a new string and don't modify the existing string

course2 = "Python programming"
print(course2.upper())  # Returns string in all caps
print(course2.lower())  # Returns string in all lowercase
print(course2.title())  # Capitalizes the first letter of each word
print(course2.strip())  # Strips any extra white space at the beginning or end
print(course2.lstrip())  # Strips extra white space from the beginning
print(course2.rstrip())  # Strips extra white space from the end of the string
print(course2.find("pro"))  # Returns the location of characters
# Python is case sensitive. When searching for characters be mindful of what you're trying to find
print(course2.replace("p", "j"))  # Replaces all insances "p" with "j"
print("pro" in course2)  # Returns true or false
print("swift" not in course)  # Returns true or false


################## Numbers ###################
x = 1  # Integar
x = 1.1  # Float
x = 1 + 2j  # Complex Number
print(10 + 3)  # Addition
print(10 - 3)  # Subtraction
print(10 * 3)  # Multiplication
print(10 / 3)  # Division
print(10 // 3)  # Division but returns a whole number
print(10 % 3)  # Modulus, or returns the remainder
print(10 ** 3)  # Exponent

# Defines a variable
x = 10
# Says that x equals itself plus 3
x = x + 3
# Short hand method to x = x + 3
x += 3


############# Working with Numbers ###################

print(round(2.9))  # Rounds a number
print(abs(-2.9))  # Absolute value
print(math.ceil(2.2))  # Returns the ceiling of a number


############### Type Conversion ##################

a = input("a: ")
print(type(a))
y = int(a) + 1
print(f"a: {a}, y: {y}")

int(x)
float(x)
bool(x)
str(x)
