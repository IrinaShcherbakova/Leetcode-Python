class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        no_path_to_zero = set()
        zero_locations = set()
        for i, num in enumerate(arr):
            if num == 0:
                zero_locations.add(i)
            else:
                no_path_to_zero.add(i)
        explored_length = len(zero_locations)
        
        while start in no_path_to_zero:
            for index in no_path_to_zero:
                if index + arr[index] in zero_locations:
                    zero_locations.add(index)
                elif index - arr[index] in zero_locations:
                    zero_locations.add(index)
            if explored_length == len(zero_locations):
                break
            explored_length = len(zero_locations)
            no_path_to_zero = no_path_to_zero.difference(zero_locations)
        
        return (False if start in no_path_to_zero else True)
            
                
                    
               
