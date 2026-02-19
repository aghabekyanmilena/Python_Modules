"""
in python almost everything is an object, most of the objects store their attributes
in dictionary called __dict__
"""

# dict of an object and class
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

p = Person("Anna", 18)
print(Person.__dict__)
print("\n ======= \n")
print(p.__dict__)

# getattr, setattr, delattr

"""
class __dict__ stores
.methods
.class attributes

Instance __dict__ -> stores instance variables
Class __dict__ -> stores methods and class variables

Python objects (by default) are basically:

Object = {
    pointer_to_class,
    __dict__ (attribute storage)
}

an object is:
.structure definition -> class
.data container -> __dict__
"""

"""
name -> local variable (parameter)
self.name -> attribute of the object

self is like this/*this in C++

in c++:
this->name = name;

in python:
self.name = name
"""

"""
p -> {
        '__class__': Person,
        '__dict__': {
        'name': 'Alice',
        'age': 25
        }
     }
The class defines structure.
The object stores data.
"""