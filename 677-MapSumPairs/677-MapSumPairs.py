# Last updated: 7/28/2025, 2:43:39 PM
class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = 0
        self.is_end = False

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.key_values = {}
        
    def insert(self, key: str, val: int) -> None:
        delta = val - self.key_values.get(key,0)
        self.key_values[key] = val
        
        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            current.value += delta
        
        current.is_end = True

    def sum(self, prefix: str) -> int:
        current = self.root
        
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]
            
        return current.value


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)