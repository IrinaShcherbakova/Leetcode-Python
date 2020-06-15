class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = [None] * 26
        for i, char in enumerate(order):
            dictionary[ord(char)-97] = i       
        for i in range(1, len(words)):
            if not self.comesBefore(words[i-1], words[i], dictionary):
                return False
        return True
    
    
    def comesBefore(self, one: str, two: str, order: List[int]) -> bool:
        length = (len(one) if len(one) < len(two) else len(two))
        for i in range(length):
            charOne = one[i]
            charTwo = two[i]
            if order[ord(charOne)-97] < order[ord(charTwo)-97]:
                return True
            if order[ord(charOne)-97] > order[ord(charTwo)-97]:
                return False
        return length == len(one)
            
        
