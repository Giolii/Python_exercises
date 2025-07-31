# Last updated: 7/30/2025, 8:19:59 PM
class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        current = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if current.children[idx] is None:
                current.children[idx] = TrieNode()
            current = current.children[idx]
        current.isEnd = True
        
    def shortest_root(self,word):
        current = self.root
        for i,c in enumerate(word):
            idx = ord(c) - ord("a")
            if current.children[idx] is None:
                return word
            current = current.children[idx]
            if current.isEnd:
                return word[:i+1]
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        word_array = sentence.split()
        trie = Trie()
        
        for word in dictionary:
            trie.insert(word)
        
        for i in range(len(word_array)):
            word_array[i] = trie.shortest_root(word_array[i])
        
        return " ".join(word_array)
            
        
        