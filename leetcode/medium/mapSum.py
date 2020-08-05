class TrieNode:
    
    def __init__(self, char: str, val: int):
        self.char = char
        self.node_sum = val
        self.children = [None] * 26
    
    def update_sum(self, val: int) -> None:
        self.node_sum += val
        
    def get_sum(self) -> int:
        return self.node_sum
        
    
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None, 0)
        self.pairs = {}
        

    def insert(self, key: str, val: int) -> None:
        old_val = (self.pairs[key] if key in self.pairs else 0)
        cur = self.root
        for char in key:
            if cur.children[ord(char)-97] == None:
                cur.children[ord(char)-97] = TrieNode(char, 0)
            cur = cur.children[ord(char)-97]
            cur.update_sum(-old_val + val)
        self.pairs[key] = val
       
        
    def sum(self, prefix: str) -> int:
        if len(prefix) == 0:
            return self.root.get_sum()
        cur = self.root
        for char in prefix: 
            if not cur.children[ord(char)-97]:
                return 0
            cur = cur.children[ord(char)-97]
        return cur.get_sum()
        
    
    
    
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
