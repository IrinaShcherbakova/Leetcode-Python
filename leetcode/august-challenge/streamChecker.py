class TrieNode:
    
    def __init__(self, val: str):
        self.val = val
        self.branches = [None] * 26
        self.end = False
        
    def makeFinal(self) -> None:
        self.end = True

    def isFinal(self) -> bool:
        return self.end
    
    
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for char in word:
            if cur.branches[ord(char)-97] == None:
                cur.branches[ord(char)-97] = TrieNode(char)
            cur = cur.branches[ord(char)-97]
        cur.makeFinal()
        

    def search(self, word: str) -> bool:
        """
        Returns if the word or its prefix is a valid word.
        """
        cur = self.root
        for char in word:     
            if not cur:
                return False
            if cur.isFinal():
                return True
            cur = cur.branches[ord(char)-97]
        return (False if not cur else cur.isFinal())
          

class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Trie()
        for word in words:
            # insert words in reversed order
            self.root.insert(word[::-1])
        self.stream = ""
        

    def query(self, letter: str) -> bool:
        self.stream = letter + self.stream
        return self.root.search(self.stream)
            
        
    

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
