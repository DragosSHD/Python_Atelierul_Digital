# Course 5 GAD
#
# Object Oriented Programming
# Decorators
# Classes and Objects
# Iterators

# Decorators allows extending the functionality of a method without altering it.
from abc import abstractmethod, ABC


def my_decorator(my_function):
    def inner(nr):
        custom_param = nr * 3
        my_function_result = my_function(custom_param)
        return my_function_result ** 2

    return inner


@my_decorator
def f1(nr):
    return nr


# my_decorated_func = my_decorator(f1)
# x = my_decorated_func(10)
x = f1(5)
print('x', x)


# The same decorator can be used on multiple functions, thus reducing the code length.
# Example Decorator with parameters:


def my_decorator_with_param(param):
    def inner_decorator(f):
        def wrapper(nr):
            print()
            f_result = f(nr)
            return f_result ** param

        return wrapper

    return inner_decorator


@my_decorator_with_param(2)
def f2(nr):
    return nr


x = f2(5)
print('x', x)


# Object Oriented Programming


# rex = Dog('Rex', 'Bulldog')
#
# rex.name = 'New Name'
# print(rex.name)
#
# new_dog = Dog.create_instance()
# print(new_dog)
# print('len = ', len(new_dog))


# Inheritance / Abstraction OOP:


class Animal:
    legs_no = 4

    def __init__(self, name, breed=None):
        self._name = name
        self.breed = breed

    @property
    def abc(self):
        return self.name

    @abc.setter
    def abc(self, name):
        self._name = name

    @abc.deleter
    def abc(self):
        del self._name

    # Method does not depend on an instance
    @staticmethod
    @abstractmethod
    def speak():
        pass

    @classmethod
    def create_instance(cls):
        return cls('Ben')

    # Equivalent for toString from JAva
    def __str__(self):
        return '<%s - Name = %s>' % (type(self).__name__, self._name)

    # Helps for debugging. Used when the object is used in other data structures.
    def __repr__(self):
        return '%s(name="%s", breed="%s")' % (type(self).__name__, self.name, self.breed)

    # Handles what happens when we use len() on our object.
    def __len__(self):
        return len(self._name)


class CustomClass:
    legs_no = 2


class Dog(Animal):

    @staticmethod
    def speak():
        print('Ham, ham!')


# First Class has priority. A class can inherit multiple classes, but the attributes of the first class in the list are
# prioritized.
class Cat(Animal, CustomClass):

    @staticmethod
    def speak():
        print('Miau, miau!')


# Example:
print('Cat no legs = ', Cat('Jolie').legs_no)

# Polymorphism

data_1 = [1, 2, 3, 4]
data_2 = 'abcdefg'
data_3 = Cat('Julie')

my_list = [data_1, data_2, data_3]
print('Lengths: ')
for data in my_list:
    print(len(data))


# Iterators

class FibonnaciIterator:
    def __init__(self, n):
        self._n = n

    def __iter__(self):
        self.iteration = 0
        self.value = 1
        self.next_value = 1
        return self

    # 1, 1, 2, 3, 5, 8, 13, 21...
    def __next__(self):
        if self.iteration < self._n:
            self.iteration += 1
            aux_value = self.value
        if self.next_value == 1:
            self.next_value += 1
        elif aux_value:
            self.value = self.next_value
            self.next_value = aux_value + self.next_value

        return aux_value


x = iter(FibonnaciIterator(10))
j = 0
for i in x:
    print('fiboNr = ', i)







