class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        hour_first = {0,1,2}
        A = sorted(A, reverse=True)
        print(A)
        
        # find largest hour
        for i, num in enumerate(A):
            if num in hour_first:
                print("first hour is %s" %num)
                is_valid_time, time = self.form_hour(num, A[0:i]+A[i+1:len(A)])
                if is_valid_time:
                    return str(num)+time
        
        return "" 
            
    
    def form_hour(self, hour: int, A: List[int]) -> tuple:
        second_dig_in_hour = {0,1,2,3} 
        
        print("in hour A %s" %A)
        is_valid_min = False
        second_dig = None
        for i, num in enumerate(A):
            if hour == 2 and num in second_dig_in_hour:
                print("second in hour is %s" %num)
                is_valid_min, minute = self.form_minute(self, A[0:i]+A[i+1:len(A)])
                if is_valid_min:
                    return True, str(num) + ':' + minute
            elif hour == 2 and num not in second_dig_in_hour:
                continue
            else:
                is_valid_min, minute = self.form_minute(self, A[0:i]+A[i+1:len(A)])
                if is_valid_min:
                    return True, str(num) + ':' + minute 
                
        return False, ""
    
    
    def form_minute(self, hour: int, A: List[int]) -> tuple:  
        print("in min A %s" %A)
        first_min = {0,1,2,3,4,5}
        if len(A) != 2:
            return False, ""
        
        first, second = A[0], A[1]
        
        if first in first_min and second in first_min:
            time = (str(first)+str(second) if first > second else str(second)+str(first))
            return True, time
        
        if first in first_min or second in first_min:
            time = (str(first)+str(second) if first in first_min else str(second)+str(first))
            return True, time
        
        return False, ""
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
