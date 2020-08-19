class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        input_str = self.char_locations(s)
        longest = ""
        for word in d:
            if self.can_be_formed(input_str, word):
                if len(word) > len(longest):
                    longest = word
                elif len(word) == len(longest) and word < longest:
                    longest = word
        return longest
    
    
    def char_locations(self, s: str) -> dict:
        locations = {}
        for i, char in enumerate(s):
            if char in locations:
                locations[char].append(i)
            else:
                locations[char] = [i]
        return locations
    
    
    def can_be_formed(self, input_str: dict, word: str) -> bool:
        last_index = -1
        for char in word:
            if char not in input_str:
                return False
            locations = input_str[char]
            next_index = 0
            while next_index < len(locations) and locations[next_index] <= last_index:
                next_index += 1
            if next_index == len(locations):
                return False
            last_index = locations[next_index]
        return True
            
            
            
            
            
            
            
            
            
            
        
         
                
