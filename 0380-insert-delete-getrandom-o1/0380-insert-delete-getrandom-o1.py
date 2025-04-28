import random

class RandomizedSet:

    def __init__(self):
        self.list = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val not in self.index_map:
            self.list.append(val)
            self.index_map[val] = len(self.list) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.index_map:
            idx = self.index_map[val]
            last_element = self.list[-1]
            self.list[idx] = last_element
            self.index_map[last_element] = idx
            self.list.pop()
            del self.index_map[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)
