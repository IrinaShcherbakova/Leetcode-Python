class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        shifted_str = [None] * len(S)
        total_shifts = shifts[-1]
        shifted_str[-1] = self.shift_by_n(S[-1], total_shifts)
        for i in range(len(shifts)-2, -1, -1):
            total_shifts += shifts[i]
            shifted_str[i] = self.shift_by_n(S[i], total_shifts)
        return "".join(shifted_str)
        
   
    def shift_by_n(self, char: str, n: int) -> str:
        n = n % 26
        if ord(char) + n <= 122:
            shifted_char_position = ord(char) + n
            return chr(shifted_char_position)
        
        n = n - (122 - ord(char)) - 1           
        shifted_char_position = ord('a') + n
        return chr(shifted_char_position)
    
    
    
