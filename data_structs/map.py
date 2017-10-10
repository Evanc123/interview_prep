
import random

class Map(object):
    def __init__(self):
        self.map = {}
        self.array = [None] * 1000
        self.length = 0

    def insert(self, key, value):
        index = self.length
        self.map[key] = (value, index)
        self.array[self.length] = key
        self.length += 1

    def get(self, key):
        if key in self.map:
            return self.map[key][0]
        else:
            return None

    def delete(self, key):
        import pdb; pdb.set_trace()
        index = self.map[key][1]
        self.array[index], self.array[self.length-1] = \
        self.array[self.length - 1], self.array[index]

        self.length -= 1
        del self.map[key]
        self.map[self.array[index]][1] = index

    def get_random_key(self):
        r = random.randint(0, self.length)
        return self.array[r]

a_map = Map()

a_map.insert(5, 3)
assert a_map.get(5) == 3
a_map.delete(5)
assert a_map.get(5) == None





class MapBad(object):
    def __init__(self, size):
        self.size = size
        self.array = [0] * size
        self.array_set = [False] * size

    def get_random_value(self):
        """ Returns a random number between 0 and self.size"""
        return random.randint(0, self.size)

    def insert(self, key, value):
        """ Inserts a the value at the given key index """
        self.array[key] = value
        self.array_set[key] = True

    def delete(self, key):
        if self.array_set[key]:
            self.array_set[key] = False

    def get(self, key):
        if self.array_set[key]:
            return self.array[key]
        else:
            return None

a = MapBad(200)

a.get_random_value()
        
