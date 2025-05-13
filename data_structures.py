from collections import deque
from array import array
from sys import getsizeof
from pprint import pprint
########################## DATA STRUCTURES #################################

################### Lists ####################

letters = ["a", "b", "c"]  # List of letters, uses square brackets and are seperated by a comma
matrix = [[0, 1], [2, 3]]  # A list of a couple lists, uses square brackets as well and each set is inside it's own set of square brackets
zeros = [0] * 5  # Prints a list with 5 0's
# Concatinates or combines the zeros list and the letters list and sets "combined" variable equal to the result of adding the two
combined = zeros + letters
print(combined)  # Prints the combined vairable, that contains the two combined lists
# Creates a list of numbers starting with 0 and going up to but not including 20
numbers = list(range(20))
print(numbers)  # Prints the numbers variable that contains the list of numbers. Doesn't include the number 20
# Creates a list to house the letters for the word "Hello World"
chars = list("Hello World") # Creates a variable called chars and sets the value equal to a list of each individual letter of the
# argument that's being passed in, which is "Hello World" 
print(len(chars))  # Prints the length of the chars variable
print(chars)  # Prints the chars variable


##################### Accessing Items #######################

# Creates a variable called letters1 and assigns a list of letters to it
letters1 = ["a", "b", "c", "d"]
# Takes the letter at the beginning of the list and replaces it with a capital A ("A")
letters1[0] = "A"
print(letters1[0])  # Prints the letter at position 0 of the list
print(letters1[-1])  # Prints the letter at the end of the list
print(letters1[0:3])  # Prints the first 3 letters in the list
numbers1 = list(range(20))  # Assigns the first 20 numbers starting with 0
print(numbers1) # Prints out the numbers1 variable that has the 20 numbers
print(numbers1[::-1])  # Prints the numbers in the list but in reverse order


######################### List Unpacking ########################

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Creates a variable called numbers2 and assigns it a list of numbers
first, second, *other = numbers2  # Unpacks the list. What's going on here
# is the first letter is listed, the second letter is listed, and then all
# of the other letters are stored in the *others variable
print(first)  # Prints the first letter
print(second) # Prints out the second letter
print(other)  # Prints the letters that are stored in the other variable, i.e. the rest of the numbers

first = numbers2[0]  # Defines the first letter in the list
second = numbers2[1]  # Defines the second letter in the list
third = numbers2[2]  # Defines the third letter in the list


###################### Looping Over a List ###########################

letters3 = ["a", "b", "c"]  # Creates a list of letters
# Use enumerate if you're wanting to get the index of the value
for index, letter in enumerate(letters3):
    # Unpacks the list for both the index and the letter in the list
    print(index, letter)  # Prints the index and letter to a tuple
    # for each iteration through the list


########################## Adding or Removing Items ###########################

letters4 = ["a", "b", "c", "d"]  # Creates a list of letters

letters4.append("d")  # Adds "d" to the end of the list
print(letters4)  # Prints the new list after appending "d"
letters4.insert(0, "-")  # Inserts "-" at the beginning of the list
print(letters4)  # Prints the new list after adding the "-"
letters4.pop(0)  # Temporarily removes the letter at index 0
print(letters4)  # Prints the new list after popping the first letter
letters4.remove("b")  # Removes the first instance of "b" from the list
print(letters4)  # Prints the new list after removing "b"
del letters4[0:3]  # Deletes all letters from index 0 -> 3
print(letters4)  # Prints the new list after deletion
letters4.clear()  # Clears or empties the entire list
print(letters4)  # Prints the new list after clearing out the entire list


###################### Finding Items in a List ################################

letters5 = ["a", "b", "c"]
print(letters5.index("a"))  # Prints out the index of the 1st instance of "a"
# print(letters5.index("d"))  # Prints out the index of "d", if it's in the list
if "d" in letters5:  # If "d" is in the list then print the index
    print(letters5.index("d"))  # If "d" is not in the list nothing is printed
print(letters5.count("a"))  # Prints the amount of times "a" is in the list


########################## Sorting a List ################################

numbers3 = [3, 51, 2, 8, 6]
numbers3.sort()  # Sorts the numbers in assending order
print(numbers3)
print(sorted(numbers3))  # Sorts and returns a new list, not a modified one
print(numbers3)
# Sorts and returns a new list in reverse order, not a modified one
print(sorted(numbers3, reverse=True))
numbers3.sort(reverse=True)  # Sorts the numbers in descending order
print(numbers3)

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    return item[1]


items.sort()  # Python doesn't know how to sort this list. We need a function
print(items)

items.sort(key=sort_item)
print(items)


############################### Lambda Functions ######################################
# Short hand way to use a function

# We're sorting the items here. When we use the lambda function, our first "item" is the parameter
# The second statement after the colon is what we're wanting to return
items.sort(key=lambda item: item[1])
print(items)


############################ Map Function ########################################

items1 = [
    ("Product1", 17),
    ("Product2", 10),
    ("Product3", 7),
]

prices = []  # Defines an empty list
for item in items1:  # Loops through each item in the items1 list
    # Adds the second item in each tuple to the prices list
    prices.append(item[1])

print(prices)  # Prints the prices


x = map(lambda item: item[1], items1)  # Uses Lambda to get the prices
for item in x:  # Loops over each item in the map object
    print(item)  # Prints out the price with each iteration


# Uses list, map, and lambda to get the prices of each item
prices = list(map(lambda item: item[1], items1))
print(prices)  # Prints the prices


########################### Filter Function #################################

items2 = [
    ("Product1", 17),
    ("Product2", 10),
    ("Product3", 7),
]

# Uses the list function and filters through the items2 list using lambda to
# get a list of products that are greater then 10
z = list(filter(lambda item: item[1] >= 10, items2))
print(z)


########################### List Comprehensions ################################

items3 = [
    ("Product1", 17),
    ("Product2", 10),
    ("Product3", 7),
]
# Defines a variable called prices1 and prints out the items in position 1 for each item
prices1 = list(map(lambda item: item[1], items3))
# Different way of writting the function above
prices2 = [item[1] for item in items3]
print(prices1)
print(prices2)

# Defines a variable called filtered1 and prints ou the items that have a price greater then or equal to 10
filtered1 = list(filter(lambda item: item[1] >= 10, items3))
# Different way of writting the function above
filtered2 = [item for item in items3 if item[1] >= 10]
print(filtered1)
print(filtered2)


############################# Zip Function ##################################

list1 = [1, 2, 3]  # Defines a list with the variable of list1
list2 = [10, 20, 30]  # Defines a list with the variable of list2

# Prints out seperate tuples with each index of the lists.
# For example, this will print out 3 seperate tuples with the results being
# (1, 10) (2, 20) (3, 30)
print(list(zip(list1, list2)))


############################# Stacks #######################################
# Stacks follow the LIFO protocol of "Last In, First Out"

browsing_session = []  # Creates an empty stack
browsing_session.append(1)  # Adds 1 to the stack
browsing_session.append(2)  # Adds 2 to the stack
browsing_session.append(3)  # Adds 3 to the stack
print(browsing_session)  # Prints out the browsing history, i.e. (1, 2, 3)
last = browsing_session.pop()  # Removes the last item in the stack
print(last)  # Prints the value of the last item that was removed
print(browsing_session)  # Prints the current browser history
if not browsing_session:  # Checks to see if the browsing history is empty
    print("No data found")


################################ Queues ####################################
# Queues follow the FIFO protocol of "First In, First Out"

# Creates a variable called queue and assigns it to an empty deque object
queue = deque([])
queue.append(1)  # Adds 1 to the queue
queue.append(2)  # Adds 2 to the queue
queue.append(3)  # Adds 3 to the queue
print(queue)  # Prints out the queue
queue.popleft()  # Removes the first number in the queue
print(queue)  # Prints out the queue after removing the first number
if not queue:  # Checks to see if the queue is empty
    print("Empty")


############################### Tuples ##################################
# Read only list, can't be modified

point = (1, 2)  # Creates a tuple called point and assigns 1 and 2 to it
print(type(point))  # Prints out the type that point is, i.e. tuple
point1 = ()  # Creates an empty tuple
print(point1)
point2 = (3, 4) + (5, 6)  # Concatonates 2 tuples -> (3, 4, 5, 6)
print(point2)
# Multiples the appearance of the items -> (7, 8, 7, 8, 7, 8)
point3 = (7, 8) * 3
print(point3)
point4 = tuple([9, 10])  # Turns a list into a tuple
print(point4)
point5 = tuple("Hello World")  # Turns a string into a tuple
print(point5)
print(point[0])  # Prints out the item at position 0
print(point[0:2])  # Prints items from position 0, up to but not including 2
x, y = point  # Unpacks the tuple by assigning each item to a variable
print(x, y)
if 10 in point:  # Checks to see if the tuple contains a certain number
    print("exists")


############################## Swapping Variables #################################

var1 = 10  # Defines a variable called var1 and assigns 10 to it
var2 = 11  # Defines a variable called var2 and assigns 11 to it

var3 = var1  # Defines a variable called var3 and copies the value of var1 to it
var1 = var2  # Assigns the value of var2 to var1
var2 = var3  # Assigns the value of var3 to var2

print("var1", var1)
print("var2", var2)

var1, var2 = var2, var1  # Shorthand method to swapping variables


################################## Array #######################################
# Arrays should be used if you're using a large set of numbers, i.e. 10000 or more
# You will need to include a typecode at the beginning of the array. This typecode
# will define the kind of data that will be stored in the array

# Creates a new array with the typecode of "i" showing that we're dealing with signed ints
numbers = array("i", [1, 2, 3])


###################################### Sets ##############################################
# A collection with no duplicates
# Unordered collection, which means you won't be able to access data points by index

numbers4 = [1, 1, 2, 3, 4]  # Creates a new list
first = set(numbers4)  # Converts the list to a set, removing any duplicates
print(first)  # Prints the new set
second = {1, 5}  # Creates a new set
second.add(5)  # Attempts to add 5 to the set if it doesn't already exist
second.remove(5)  # Removes 5 from the list
print(len(second))  # Prints the length of the "second" list
print(first | second)  # Combines the 2 sets, excluded duplicates between the 2
print(first & second)  # Returns all numbers that are in both sets
print(first - second)  # Returns numbers from the first set, but not the second
# Returns items that are either in the first or second set, not both
print(first ^ second)
if 1 in first:  # Checks to see if 1 is in the first set
    print("Yes")


################################## Dictionaries #########################################
# Used to map a key to a value, i.e. with a phone book the persons name is the key
# and the persons phone number is the value

point6 = {"x": 1, "y": 2}  # Creates a new dictionary
point7 = dict(x=1, y=2)  # Creates a new dictionary

print(point6["x"])  # Prints the value associated with key "x"
point6["x"] = 10  # Changes the value associated with key "x" to 10
print(point6)

point6["z"] = 20  # Assigns a new key value pair of "z": 20 to the dictionary
print(point6)

if "a" in point6:  # Checks to see if "a" is located in the dictionary
    print(point6["a"])

# Checks to see if "a" is located in the dictonary, if not 0 is returned
print(point6.get("a", 0))

del point6["x"]  # Deletes the value associated with the value of key "x"
print(point6)

for key in point6:  # Prints out the key value pairs in the dictionary
    print(key, point6[key])

for key, value in point6.items():  # A different way to print out key value pairs
    print(key, value)


############################ Dictionary Comprehensions #################################

values = {}  # Defines an empty dictionary
for x in range(5):  # Loops over each value in the range of 5, multiplies it by 2 and adds it to the dictionary
    values[x] = x * 2

# Different way to write the statement above
values = {x: x * 2 for x in range(5)}
print(values)


########################### Generator Expressions ##################################

values1 = (x * 2 for x in range(1000))  # Creates a generator object
# Prints out the size of the generator object
print("gen:", getsizeof(values1))


############################## Unpacking Operator ####################################

numbers5 = [1, 2, 3]  # Defines a new list
print(*numbers5)  # Prints out all of the numbers with no commas in between
values2 = list(range(5))  # Defines a variable that stores the numbers 1-4
print(values2)
# Defines a variable that unpacks the values 1-4 and each individual letter in "Hello"
values3 = [*range(5), *"Hello"]
print(values3)

third = [1, 2]
fourth = [3]
# Unpacks the values in the third list, adds "a", unpacks the fourth list and the word "Hello"
values4 = [*third, "a", *fourth, *"Hello"]
print(values4)

fifth = {"x": 1}
sixth = {"x": 10, "y": 2}
# Defines a variable called combined and unpacks the fifth dictionary, sixth dictionary, and the new "z" key value pair
combined = {**fifth, **sixth, "z": 1}
print(combined)


############################### Exercise ######################################

sentence = "This is a common interview question"
# Turns all characters to lowercase so that there's no duplicates
sentence1 = sentence.lower()

storage = {}  # Defines an empty dictionary

for letter in sentence1:  # Loops through each letter in the sentence
    if letter != " ":  # Checks to make sure that the character isn't a space
        if letter not in storage:  # First checks to see if the letter is in the dictionary
            # If the letter doesn't exist it's added to the dictionary
            storage[letter] = 1
        else:  # If the letter already exists the the value is increased by 1
            storage[letter] += 1

# Loops through each key/value pair in the dictionary and prints out each pair
for key, value in storage.items():
    print(key, value)

most_repeated = max(storage, key=storage.get)  # Find the most repeated letter
# Prints out the most repeated letter with the amount of occurances
print(most_repeated, storage[most_repeated])


######################## Another Solution ################################

another_sentence = "This is a common interview question"

char_frequency = {}  # Defines an empty dictionary
for char in sentence:  # Loops through each letter in the sentence
    if char in char_frequency:  # Checks to see if the letter exists in the dictionary
        char_frequency[char] += 1  # If so, the occurance is increased by 1
    else:  # If the letter doesn't exist
        char_frequency[char] = 1  # Add it to the dictionary and set value to 1

char_frequency_sorted = sorted(  # Sorts the dictionary and store the info in a variable called char_frequency_sorted
    # Gets each item and sorts in descending order based on the value
    char_frequency.items(), key=lambda kv: kv[1], reverse=True)
# Prints out the first item, which will be the highest value
print(char_frequency_sorted[0])
