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
        Returns if the word is in the trie.
        """
        cur = self.root
        for i, char in enumerate(word):     
            if cur.branches[ord(char)-97] == None:
                return False
            if i == len(word) - 1:
                return cur.branches[ord(char)-97].isFinal()
            cur = cur.branches[ord(char)-97]
          
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for i, char in enumerate(prefix):
            if cur.branches[ord(char)-97] == None:
                return False
            cur = cur.branches[ord(char)-97]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
