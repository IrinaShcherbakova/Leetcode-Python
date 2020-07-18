class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res, dependOn, influence = [], [], []
        independent = set()
        
        for i in range(numCourses):
            dependOn.append([])
            influence.append([])
            independent.add(i)
            
        for pair in prerequisites:
            second = pair[0]
            first = pair[1]
            independent.discard(second)
            influence[first].append(second)
            dependOn[second].append(first)
            
        # print(dependOn)
        # print(influence)
        
        if len(independent) == 0:
            return res
        
        while len(independent) > 0:
            course = independent.pop()
            # print("course is %s" %course)
            res.append(course)
            dependant = influence[course]
            for influenced in dependant:
                dependOn[influenced].remove(course)
                if len(dependOn[influenced]) == 0:
                    independent.add(influenced)
        if len(res) == numCourses:
            return res
        return []
                    
                
            
        
