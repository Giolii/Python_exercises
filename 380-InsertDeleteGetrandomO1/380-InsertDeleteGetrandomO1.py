# Last updated: 6/29/2025, 2:17:07 PM
class RandomizedSet:

    def __init__(self):
        self.values = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:            
            return False
        self.indices[val] = len(self.values)
        self.values.append(val)
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        end = len(self.values) - 1
        idx_value = self.indices[val]
        
        self.values[idx_value] = self.values[end]
        self.indices[self.values[end]] = idx_value
        self.values.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        idx = int(random.random() * len(self.values)) 
        return self.values[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()