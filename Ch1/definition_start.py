# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
    def _init_(self,title):
        self.title = title
# A Class is like an object constructor, or a "blueprint" for creating objects.
#The examples above are classes and objects in their simplest form, and are not really useful in real life applications.To understand the meaning of classes we have to understand the built-in __init__() function. All classes have a function called __init__(), which is always executed when the class is being initiated. Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
# TODO: create instances of the class
b1 = Book("Brave New World")
b2 = Book("War and Peace")


# TODO: print the class and property
print(b1)
print(b1.title)