class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        ranges = [[0,0], [0,9], [10,99], [100,999], [1000,9999], [10000,99999],[100000,999999], [1000000,9999999], [10000000,99999999], [100000000,999999999]]
        start = ranges[N][0]
        step = (1 if start == 0 else ranges[N][0])
        end = ranges[N][1]
        res = []
        self.build_numbers_in_range(step, start, end, K, res)
        return res
    
    
    def build_numbers_in_range(self, step: int, start: int, end: int, K: int, res: List[int]) -> None:
        if start > end:
            return
        
        start_string = str(start)
        length = len(start_string)
        leading_digit = start_string[0]
        numbers_in_range = []
        self.build_number(leading_digit, length, K, numbers_in_range)
        if numbers_in_range:
            res += numbers_in_range
        
        # recurse further with the next starting digit
        return self.build_numbers_in_range(step, start+step, end, K, res)
    
    
    def build_number(self, num: str, length: int, K: int, res: List[int]) -> None:
        if len(num) == length:
            res.append(int(num))
            return
        
        last_digit = num[-1]
        
        # recurse by adding K to num
        addition = int(last_digit) + K
        if addition <= 9:
            plus_k = num + str(addition)
            self.build_number(plus_k, length, K, res)
            
        # recurse by subtracting K from num
        subtract = int(last_digit) - K
        if subtract >= 0 and K > 0:
            minus_k = num + str(subtract)
            self.build_number(minus_k, length, K, res)
        
        return
        
        
        
        
            
    
    
    
        
                 
