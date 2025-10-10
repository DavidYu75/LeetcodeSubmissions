import random
class RandomizedSet:

    def __init__(self):
        self.seen = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.seen:
            return False
        
        self.seen[val] = len(self.arr)
        self.arr.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.seen:
            return False
        
        last_val = self.arr[-1]
        val_index = self.seen[val]

        self.arr[-1] = val
        self.arr[val_index] = last_val
        self.seen[last_val] = val_index

        self.arr.pop()
        del self.seen[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()