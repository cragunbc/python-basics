################################### Classes #######################################
# Blueprint for creating new objects
# Objects are an instance of a class

# i.e. Class: Human
# i.e. Objects: John, Mary, Jack


################################### Creating Classes #######################################
# Classes use Pascal naming convention, Uppercase letter for each new word. No underscore
# By convention the parameter that we put in the functions is "self", it a reference to the class

class Point:  # Use the "class" definition and name the class in Pascal naming convention
    def draw(self):  # Defines a function for the class called draw that has a parameter of "self"
        # Whenever this function is called the word "draw" is printed on the console
        print("draw")


point = Point()  # Creates a variable called point to assign a call to the Point class
print(type(point))  # Checks what type of class point is
# Checks to see if the object is an instance of the class
print(isinstance(point, Point))


####################################### Constructors ############################################

class Point1:
    # This is the constructor. It's executed whenever we create a new object. Add self
    # is a reference to the current point object. Self is the first parameter that's passed
    # in among other parameters
    def __init__(self, x, y):
        self.x = x  # self is used to define x
        self.y = y  # self is used to define y

    def draw(self):  # Once again uses the self parameter
        # Prints out the varaibles that are defined above
        print(f"Point ({self.x}, {self.y})")


point1 = Point1(1, 2)  # Creates an object called point1
point1.draw()  # Runs the draw method from the object that we created


###################################### Class vs Instance Attributes ######################################
# The difference between class attributes and instance attributes are the following
# Class Attributes: Characteristics that are shared among all of the objects, i.e. in the example below the
# attribute of default_color = "red" will be available to all objects

# Instance Attributes: Attributes are are specific to the object. In the example below if we defined the
# arguments of (1, 2) to a new object then those values would be specific to that object. If we created
# an additional object then the values assigned to it would be specific to that object

class Point2:
    default_color = "red"  # Class attributes that's shared with all instances of this class

    def __init__(self, x, y):
        self.x = x  # Instance attribute, unique for each object
        self.y = y  # Instance attribute, unique for each object

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point2 = Point2(1, 2)  # Instance attributes
another = Point2(3, 4)  # Instance attributes
point2.draw()
another.draw()
point2.default_color  # Class attribute


################################# Class vs Instance Methods ########################################
# Similar to the class and instance attributes, Instance Methods and Class methods are defined below
# Instance Methods are shared and executed against an object and need an object in order to run.

# Class Methods: Run on the class itself and not on an object. They can be used to create factory functions
# modify class state or access class-level data

class Point3:
    def __init__(self, x, y):  # Instance method. Able to be operated on by any object
        self.x = x
        self.y = y

    # Can't be accessed by an object, only from the class itself
    @classmethod  # Used to define a class method
    def zero(cls):  # Instead of "self" we use "cls" which is a reference to the class
        return cls(0, 0)

    def draw(self):  # Instance method
        print(f"Point ({self.x}, {self.y})")


point3 = Point3(1, 2)  # Calling an instance method
point3.draw()
point4 = Point3.zero()  # Calling the class method
point4.draw()


####################################### Magic Methods #########################################
# Magic methods are defined by a double underline at the beginning and end. They're also referred
# to as dunder methods (double underline). They can give our class "special powers" such as defining
# how an object is created and making objects behave like built in types

class Point4:

    def __init__(self, x, y):
        self.x = x  # Instance attribute
        self.y = y  # Instance attribute

    def __str__(self):  # Magic method to print out the variables defined above instead of getting the
        # memory location of the object. Prints out the object
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point6 = Point4(8, 10)  # Uses the new __str__ method to get the point object
print(point6)  # Prints out the variable that's holding the __str__ object
# Different way of writting the line above to print out the point object
print(str(point6))


##################################### Comparing Objects ###########################################
# If you have two objects that have the same values and you try to compare them using the == operator
# you will get a response that they are not equal. The reason being is because with you use the ==
# operator you're comparing the places in memory that the values are being stored. Since they're two
# different instances they will be stored in different locations. To compare two objects we're going to
# have to use the __eq__ magic method

class Point5:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):  # We define the function to compare the two objects. We'll use self as one of the
        # parameters and other to represent the other parameter. What this is doing is comparing the two objects
        # and their values to see if they're equal. If they're equal then we will get a boolean value of true. If
        # they aren't equal then we'll get a boolean value of false
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):  # We define the function to see if one of the objects is greater then the other. Like
        # the case above we'll use self and other. If self is greater other then we'll get true. If it isn't then
        # we'll get fales
        return self.x > other.x and self.y > other.y


point7 = Point5(8, 10)  # First instance of the object
point8 = Point5(7, 2)  # Second instance of the object
# Since the two values provided in the two objects above are the same we'll get true
print(point7 == point8)
# Since the values in point7 are greater then point8 we'll get true
print(point7 > point8)


########################### Performing Arithmetic Operations ##################################

class Point6:
    def __init__(self, x, y):  # Creates a constructor that takes the parameters of self, x and y
        self.x = x  # Defines the instance variable of self.x and assigns the value of x to it
        self.y = y  # Defines the instance variable of self.y and assigns the value of y to it

    def __add__(self, other):  # Creates a magic method that takes to parameters of self and other
        # Returns the values of adding the first number of self and other together and the second
        # number of both self and other together
        return Point6(self.x + other.x, self.y + other.y)


# Creates a new instance of the Point6 class and passes in 10 and 20 as arguments
point9 = Point6(10, 20)
# Creates a new instance of the Point6 class and passes in 1 and 2 as arguments
point10 = Point6(1, 2)
# Creates a new variable called combined that will use the __add__ magic method to add the arguments
# Because there's a "+" and we've defined the __add__ magic method, python knows automatically to
# call the __add__ magic method. If we hadn't defined the __add__ magic method then a TypeError
# would've been raised
combined = point9 + point10
# Print the result of the combined variable
print(combined.x)


################################## Making Custom Containers #############################################
# A container is an object that holds or contains other objects. These are data structures that can store
# a collection of elements - either of the same type or different types.
# If you can loop through it (for item in container:), it's usually a container. You can also often use the
# in keyword to check for membership

# Different container types:
# List:
#   - Ordered, mutable collection. Elements can be accessed by index
#   - my_list = [1, 2, 3]
# Tuple:
#   - Ordered, immutable collection. Like a list, but cannot be changed
#   - my_tuple = ("apple", "banana", "cherry")
# Dict:
#   - Key/value pairs. Useful for fast lookup and mapping
#   - my_dict = {"name": "Alice", "age": 30}
# Set:
#   - Unordered collection of unique elements
#   - my_set = {1, 2, 3, 4}
# Str:
#   - Technically a container of characters (immutable)
#   - my_string = "hello"

class TagCloud:  # Creates a new class called TagCloud
    def __init__(self):  # Creates a new constructor that takes self as the parameter
        self.tags = {}  # Creates a tags object that is assigned to an empty dictionary

    def add(self, tag):  # Defines an add function that takes the parameters of self, and tag
        # Calls the tags object of the instance of the class (self) in all lowercase. If the
        # tag isn't present then 0 is returned and 1 is added. If the tag is present in the
        # dictionary then we will get it and add 1 to it
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    # Defines a magic method to get the items out of the dictionary. Self and tag are the parameters
    # that are needed. If the tag exists in the dictionary then it is returned. If the tag doesn't
    # exist then 0 is returned
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    # Defines a magic method of __setitem__ to set the amount of times that a particular tag appears
    # in the dictionary. Self, tag, and count are the parameters that are required. The method will
    # take the tag that you pass in and assign it the count variable that you also passed in
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    # Defines a magic method of __len__ to get the length of the dictionary. In other words, it will
    # return the amount of key/value pairs that are in the dictionary
    def __len__(self):
        return len(self.tags)

    # The __iter__ magic method is used when you want to iterate over an instace of a class using a
    # for loop or a list.
    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud.add("python")  # Adds python as a key in a key/value pair
cloud.add("python")  # Adds python as a key in a key/value pair
cloud.add("Python")  # Adds python as a key in a key/value pair
cloud.add("C#")  # Adds C# as a key in a key/value pair
print(cloud.__setitem__("python", 10))
# Prints the length of how many tags of "python" are in the dictionary
print(cloud.__getitem__("python"))
# Prints the amount of times that C++ is in the dictionary
print(cloud.__getitem__("C++"))
print(cloud.__len__())  # Prints the length of how many tags are in the dictionary
# Prints out the different keys that are found in the dictionary
print(list(cloud.__iter__()))
print(cloud.tags)  # Prints out the whole dictionary will all the key/value pairs


############################## Private Members ########################################
# Prefessing all instances of the dictionary in this class with a double underline ("__")
# then we are making that dictionary private. Even though we can still access it from the outside
# this is a practice to prevent access to these private members

class TagCloud1:  # Creates a new class called TagCloud
    def __init__(self):  # Creates a new constructor that takes self as the parameter
        self.__tags = {}  # Creates a tags object that is assigned to an empty dictionary

    def add(self, tag):  # Defines an add function that takes the parameters of self, and tag
        # Calls the tags object of the instance of the class (self) in all lowercase. If the
        # tag isn't present then 0 is returned and 1 is added. If the tag is present in the
        # dictionary then we will get it and add 1 to it
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    # Defines a magic method to get the items out of the dictionary. Self and tag are the parameters
    # that are needed. If the tag exists in the dictionary then it is returned. If the tag doesn't
    # exist then 0 is returned
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    # Defines a magic method of __setitem__ to set the amount of times that a particular tag appears
    # in the dictionary. Self, tag, and count are the parameters that are required. The method will
    # take the tag that you pass in and assign it the count variable that you also passed in
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    # Defines a magic method of __len__ to get the length of the dictionary. In other words, it will
    # return the amount of key/value pairs that are in the dictionary
    def __len__(self):
        return len(self.tags)

    # The __iter__ magic method is used when you want to iterate over an instace of a class using a
    # for loop or a list.
    def __iter__(self):
        return iter(self.tags)


cloud1 = TagCloud1()  # Creates a new instance of the TagCloud1 class
# Prints out all of the attributes of the class to the terminal. This will return a variable called
# "_TagCloud1__tags" which we can then print out to get access to the dictionary, even though access
# is being prevented
print(cloud1.__dict__)
print(cloud1._TagCloud1__tags)  # Prints out the contents of the dictionary
# cloud1.add("python") -> Adds the python tag to the dictionary
# cloud1.add("python") -> Adds the python tag to the dictionary
# cloud1.add("python") -> Adds the python tag to the dictionary
# print(cloud1.__tags["PYTHON"]) -> Gives us an error because everything is being stored as lower case


################################ Properties ######################################
# A Property is a special kind of attribute that allows you to control access to instance variables.
# It's commonly used to define getters, setters, and deleters for an attribute, while still allowing it
# to be accessed like a regular variable

# Properties take two parameters to get and set the method

class Product:  # Creates a new class called Product that represents an item with a price
    def __init__(self, price):  # Creates a contructor that takes self and price as the parameters
        self.price = price  # Calls the setter method below to set the price

    @property  # @property decorator declares a property
    def price(self):
        return self.__price  # Returns the price value

    @price.setter  # Defines a setter for the Product class
    def price(self, value):  # Takes the parameters of self and value
        if value < 0:  # First uses validation to see if the value is greater then 0
            # If the value is less then 0 a ValueError is raised
            raise ValueError("Price cannot be negative.")
        # If the value is greater then 0 the value of the value parameter is set for the price
        self.__price = value


product = Product(10)
print(product.price)


################################# Inheritance ###########################################
# Inheritance is a way to define common behavior that can be used among different classes so that we don't
# have to repeart ourselves.

class Animal:  # Defines a class called Animal. This is the class that the other class will inherit functions
    # and attributes from
    def __init__(self):  # Defines a constructor
        self.age = 1  # Sets the age of the instance of the class to 1

    def eat(self):  # Defines a function called eat that takes the parameter of self
        print("Eat")  # Prints out the word "Eat" whenever it is called


class Mammal(Animal):  # Defines a class called Mammal that inherits all the methods and attributes of the Animal class
    def walk(self):  # Defines a function called walk that takes the parameter of self
        print("Walk")  # Prints out the word "Walk" when it is called


class Fish(Animal):  # Defines a class called Fish that inherits all the methods and attributes of the Animal class
    def swim(self):  # Defines a function called swim that takes the parameter of self
        print("Swim")  # Prints out the word "Swim" when it si called


m = Mammal()  # Defines a new object called m and sets it equal to the Mammal class
m.eat()  # Prints out the word "Eat" that is being inherited from the Animal class
print(m.age)  # Prints out the age that is being inherited from the Animal class


#################################### Object Class ###########################################
# All classes area subclass of the object class

# Prints out True if the m object is an instance of the Mammal class
print(isinstance(m, Mammal))
# Prints out True if the m object is an instance of the object class
print(isinstance(m, object))
o = object()  # Defines a new object
# Checks to see if the Mammal class is a subclass of the Animal class
print(issubclass(Mammal, Animal))
# Checks to see if the Mammal class is a subclass of the object class
print(issubclass(Mammal, object))


###################################### Method Overriding ########################################
# Method overriding is a concept where a subclass provides a specific implementation of a method that
# is already defined in its parent class. The overridden method in the child class has the same name,
# parameters, and return type as the method in the parent class. This allows the child class to
# customize or extend the bahavior of a method defined in the parent class
# Only methods can be overriden, attributes do not have the ability to be overriden

class Animal1:  # Defines a class called Animal1 that is the parent class
    def __init__(self):  # Defines a constructor that takes the paramenters of self
        self.age = 1  # Sets the age of the instance of the class to 1

    def eat(self):  # Defines a function called eat that takes the parameter of self
        print("Eat")  # Prints out the word "Eat" when it is called


class Mammal1(Animal1):  # Defines a class called Mammal1 that inherits all attributs and functions from Animal1
    def __init__(self):  # Defines a constructor for the Mammal1 class
        super().__init__()  # If we didn't have this here to call the constructor of the bass class
        # then the entire constructor for the base class would be replaced with the new code here.
        # This calls the constructor from the bass class so that we're still using the methods from the bass class
        # but extending it to also include the weight attribute
        self.weight = 2  # Defines an attribute for the Mammal1 class

    def walk(self):  # Defines a method called walk that takes the parameter of self
        print("Walk")  # Prints out the word "Walk" when it is called


class Fish1(Animal1):  # Defines a class called Fish1 that inherits all the attributes and functions from Animal1
    def swim(self):  # Defines a method called swim that takes the parameter of self
        print("Swim")  # Prints out the word "Swim" when it is called


m1 = Mammal1()  # Creates a new object of the Mammal1 class called m1
print(m1.age)  # Prints out the age attribute that is inherited from the Animal1 class
# Prints out the weight attribute that is defined in the contructor of the Mammal1 class
print(m1.weight)


############################### Multi level Inheritance ######################################
# Multi level inheritance is where a class is derived from another derived class. Just because
# you can do inheritance doesn't mean that you always should. Keep your inheritance to 1 or two
# levels deep, anymore then that will cause confusion and issues in your program down the road
# because of the complexity that you're trying to implament


############################### Multiple Inheritance ###################################
# Multiple Inheritance is where you will inherit the attributes and methods from multiple different classes

class Employee:  # Creates a class called Employee
    def greet(self):  # Creates a greet method that takes the parameter of self
        # Prints the words "Employee Greet" when called upon
        print("Employee Greet")


class Person:  # Creates a class called Person
    def greet(self):  # Creates a greet method that takes the parameter of self
        # Prints the words "Person Greet" when called upon
        print("Person Greet")


# Creats a new class called manager that inherits all the attributes and methods of both the Employee and Person classes
class Manager(Employee, Person):
    pass


manager = Manager()  # Creates a new object of the Manager class called manager
manager.greet()
# When this method is executed it follows the following steps:
# 1. First looks at the Manager class to see if there's a greet method, if so it executes it
# 2. If the Manager class doesn't have a greet method, it would use the first class that's being inherited, in this case the Employee class
# 3. If the Employee class doesn't have a greet method, it will use the second inherited class, in this case the Person class

# This isn't good practice because the two classes that are being inherited have methods that are very similar. Because of this
# it makes multiple inheritance a thing that we shouldn't be doing because it can cause confusion in the code. When you use multiple
# inheritance you want to do it wil classes that aren't related at all so that there's no overlap in what methods do, such as below


class Flyer:  # Creates a class called Flyer
    def fly(self):  # Defines a method called fly that takes the parameter of self
        pass  # Placeholder phrase that does nothing when executed. Used when you want to run the program with no code in the method


class Swimmer:  # Creates a class called Swimmer
    def swim(self):  # Defines a method called swim that takes the parameter of self
        pass  # Placeholder phrase that does nothing when executed. Used when you want to run the program with no code in the method


# Creates a class called FlyingFish that inherits the attributes and methods from the Flyer and Swimmer class
class FlyingFish(Flyer, Swimmer):
    pass  # Placeholder phrase that does nothing when executed. Used when you want to run the program with no code in the method

# This implamentation of multiple inheritance is a good example that doesn't have methods that overlap each other.
