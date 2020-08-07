class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        dict.sort(key=len)
        words = sentence.split()
        for i in range(len(words)):
            words[i] = self.find_root(words[i], dict)
        return " ".join(words)
    
    
    def find_root(self, word: str, dict: List[str]) -> str:
        for root in dict:
            if word.startswith(root):
                return root
        return word
        
