class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        forward = backward = 0
        #compute forward distance
        i = start
        while i != destination:
            forward += distance[i]
            i += 1
            if i == len(distance):
                i = 0   
        #compute backward distance
        j = destination
        start = (0 if start == 1 else start)
        while j != start:
            backward += distance[j]
            j += 1
            if j == len(distance):
                j = 0
        return (forward if forward < backward else backward)
