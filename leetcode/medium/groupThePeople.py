class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(groupSizes)):
            if groupSizes[i] < 0:
                continue
            group = [i]
            j = i+1
            while len(group) < groupSizes[i]:
                if groupSizes[j] == groupSizes[i]:
                    group.append(j)
                    groupSizes[j] = -1 * groupSizes[j]
                j += 1
            res.append(group)
        return res
            

        
