#-------------------------------------------------------------------------------
'''001.
   Join two dictionaries (Python 3.5+).
   If the keys of dictionaries are the same, they will be owerrided from left to rigth.
'''
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}               # z ==  {'c': 4, 'a': 1, 'b': 3}

#-------------------------------------------------------------------------------
'''002.
   The dictionary has get() method, which returns value if key exist or default value if not.
'''
users = {382: "Alice", 590: "Bob", 951: "Dilbert"}
users.get(999, 'Unkknown_User')

#-------------------------------------------------------------------------------
'''003.
   Using of the namedtuples is shorter then classes creation.
   # namedtuples are immutable as ordinary tuple.
'''
from collections import namedtuple
Car = namedtuple('Car', 'color mileage')  # объявление Namedtuple
my_car = Car('red', 3812.4)               # Car ведет себя как класс
my_car.color                              # 'red'
my_car.mileage                            # 3812.4
my_car                                    # Car(color='red' , mileage=3812.4)
my_car.color = 'blue'                     # AttributeError: can't set attribute

#-------------------------------------------------------------------------------
'''004.
   Different methods of flag checking.
'''
x, y, z = 0, 1, 0
if x == 1 or y == 1 or z == 1:
    pass
if 1 in (x, y, z):
    pass
if x or y or z:
    pass
if any((x, y, z)):
    pass

#-------------------------------------------------------------------------------
'''005.
   The nice method to view dict content.
'''
import json
my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(json.dumps(my_mapping, indent=4, sort_keys=True))
{
    "a": 23,
    "b": 42,
    "c": 12648430
}

#-------------------------------------------------------------------------------
'''006.
   Function argument unpacking.
'''
def myfunc(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}
myfunc(*tuple_vec)   # 1, 0, 1
myfunc(**dict_vec)   # 1, 0, 1
#-------------------------------------------------------------------------------
