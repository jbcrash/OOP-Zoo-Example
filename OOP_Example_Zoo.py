'''
Author: Josh Bellingham
Version: 04/20/22
Description: A program to make a zoo based on classes and subclasses
'''

import functools
import re

class Animal:
    '''Defines the 'animal' class'''
    def __init__(self):
        self.__number_of_legs = 4
        self.__number_of_hands = 0

    def look(self):
        '''a function to see the attributes of animals'''
        return f"Number of hands: {self.__number_of_hands}, Number of legs: {self.__number_of_legs}"


class Bird:
    '''Defines the 'bird' class'''
    def __init__(self):
        self.__number_of_legs = 2
        self.__number_of_wings = 2

    def look(self):
        '''a function to see the attributes of birds'''
        return f"Number of wings: {self.__number_of_wings}, Number of legs: {self.__number_of_legs}"

class Feline(Animal):
    '''Feline subclass of animal class'''
    def __init__(self):
        Animal.__init__(self)
        self.__characteristic = "Felines belong to the cat family"

    def look(self):
        '''a function to see the attributes of animal'''
        return super().look() + "\n" + self.get_characteristic()

    def get_characteristic(self):
        '''a function to get the characterists of the animals'''
        return self.__characteristic

class Tiger(Feline):
    '''Tiger subclass of feline class'''
    def __init__(self):
        Feline.__init__(self)
        self.__characteristic = "Tigers can roar and are lethal predators"

    def get_characteristic(self):
        '''a function to get the characterists of the animals'''
        return super().get_characteristic() + "\n" + self.__characteristic

class WildCat(Feline):
    '''WildCat subclass of feline class'''
    def __init__(self):
        Feline.__init__(self)
        self.__characteristic = "Wild cats can climb trees"

    def get_characteristic(self):
        '''a function to get the characterists of the animals'''
        return super().get_characteristic() + "\n" + self.__characteristic

class Canine(Animal):
    '''Canine subclass of animal class'''
    def __init__(self):
        Animal.__init__(self)
        self.__characteristic = "Canines belong to the dog family"

    def look(self):
        '''a function to see the attributes of animal'''
        return super().look() + "\n" + self.get_characteristic()

    def get_characteristic(self):
        '''a function to get the characterists of the animals'''
        return self.__characteristic

class Wolf(Canine):
    '''Wolf subclass of canine class'''
    def __init__(self):
        Canine.__init__(self)
        self.__characteristic = "Wolves hunt in packs and have a leader"

    def get_characteristic(self):
        '''a function to get the characterists of the animals'''
        return super().get_characteristic() + "\n" + self.__characteristic

class FlightBird(Bird):
    '''FlightBird subclass of bird class'''
    def __init__(self):
        Bird.__init__(self)
        self.__characteristic = "Flight birds fly and hunt for food"

    def look(self):
        '''a function to see the attributes of animal'''
        return super().look() + "\n" + self.get_characteristic()

    def get_characteristic(self):
        '''a function to get the characterists of the animals'''
        return self.__characteristic

class Eagle(FlightBird):
    '''Eagle subclass of FlightBird class'''
    def __init__(self):
        FlightBird.__init__(self)
        self.__characteristic = '''Eagles fly extremely high
and can see their prey from high up in the sky'''

    def get_characteristic(self):
        '''a function to get the characterists of the animals'''
        return super().get_characteristic() + "\n" + self.__characteristic

class Zoo:
    '''A class to define a zoo that holds a set amount of snimals and birds'''
    def __init__(self):
        self.__animal_list = []
        self.__bird_list = []

    def add(self, living_thing):
        '''Checks if the thing being added is an animal or bird'''
        if not isinstance(living_thing, Animal) and not isinstance(living_thing, Bird):
            raise Exception ("Only animals and birds can be added")
        try:
            if isinstance(living_thing, Animal): #subclass for animal and bird
                if len(self.__animal_list) < 2:
                    if len(list(filter(lambda x : type(living_thing) == type(x), self.__animal_list))) == 0:
                        self.__animal_list.append(living_thing)
                        print("Animal added")
                    else:
                        raise KeyboardInterrupt()
                else:
                    print("Zoo full for animals")

                if isinstance(living_thing, Bird):
                    if len(self.__bird_list) < 2:
                        self.__bird_list.append(living_thing)
                        print("Bird added")
                    else:
                        print("Zoo full for birds")
        except KeyboardInterrupt:
            print("Animal already exists")
        except Exception as err:
            print("Error in adding animal/bird")
            print(err.__class__)
        else:
            print("Added successfully")

    def looking(self):
        '''a function to see the animals and birds in the zoo'''
        print(Zoo.__look_at_member(self.__animal_list + self.__bird_list))

    def find_canine(self):
        '''Function searches animal list for canines'''
        print(Zoo.__look_at_member(
            list(filter(lambda a: isinstance(a, Canine), self.__animal_list))))

    def find_tiger(self):
        '''Function searches animal list for Tiger using regex'''
        print(Zoo.__look_at_member(
            list(filter(lambda b: re.search("Tiger", b.look()), self.__animal_list))))

    @staticmethod
    def __look_at_member(lst):
        '''Static method for looking at animals'''
        if len(list(lst)) == 0:
            return ""
        print()
        str1 = functools.reduce(lambda a, b: a + '\n\n' + b,
                    map(lambda l: l.look(), list(lst)))
        return str1

zoo = Zoo()

zoo.add(Wolf())
zoo.add(Tiger())

zoo.find_canine()
zoo.find_tiger()
