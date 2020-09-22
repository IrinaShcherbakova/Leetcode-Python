class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        km = {}
        for trip in trips:
            num_passeng, start, end = trip[0], trip[1], trip[2]
            if start in km:
                km[start].append(num_passeng)
            else:
                km[start] = [num_passeng]
            if end in km:
                km[end].append(num_passeng * -1) 
            else:
                km[end] = [num_passeng * -1]
        total_passeng = 0
        print(km)
        for point in sorted(km):
            for num in km[point]:
                total_passeng = max(0, total_passeng + num)
            print(total_passeng)
            if total_passeng > capacity:
                return False
        return True
        
        
            
