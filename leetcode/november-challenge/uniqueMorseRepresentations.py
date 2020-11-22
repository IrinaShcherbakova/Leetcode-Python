class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];
        
        unique = set()
        for word in words:
            cur = ""
            for char in word:
                index = ord(char) - 97
                cur += morse_code[index]
            unique.add(cur)
        return len(unique)
