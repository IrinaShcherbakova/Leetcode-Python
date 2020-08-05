class TrieNode: 
    
    def __init__(self, val: str):
        self.val = val
        self.children = [None] * 26
        self.leaf = False
        
    def makeLeaf(self) -> None:
        self.leaf = True
        
    def isLeaf(self) -> bool:
        return self.leaf
    
    

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for char in word:
            if cur.children[ord(char)-97] == None:
                cur.children[ord(char)-97] = TrieNode(char)
            cur = cur.children[ord(char)-97]
        cur.makeLeaf()
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.foundMatchingWord([self.root], word)
    
        
    def foundMatchingWord(self, variants: List[TrieNode], word: str) -> bool:
        for path in variants:
            if self.traverseTrie(path, word):
                return True
        return False
                
        
    def traverseTrie(self, root: TrieNode, word: str) -> bool:
        if len(word) == 0:
            return root.isLeaf()
        cur = root
        newVariants = []
        for i, char in enumerate(word):
            if char == '.':
                for child in cur.children:
                    if child is not None:
                        newVariants.append(child)
                return self.foundMatchingWord(newVariants, word[i+1:len(word)])
            elif cur.children[ord(char)-97] is None:
                return False
            elif i + 1 == len(word):
                return cur.children[ord(char)-97].isLeaf()
            cur = cur.children[ord(char)-97]
        return False
        
        
        
        
        
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
