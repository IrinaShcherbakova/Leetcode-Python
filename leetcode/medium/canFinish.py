class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        canTake = set()
        for i in range(numCourses):
            canTake.add(i)
        
        indegree = [0] * numCourses
        adjList = {}
        for pair in prerequisites:
            course, prereq = pair[0], pair[1]
            indegree[course] += 1
            if prereq in adjList:
                adjList[prereq].append(course)
            else:
                adjList[prereq] = [course]
            canTake.discard(course)

        totalFinished = 0
        # print("zero indegree %s" %totalFinished)
        while len(canTake) > 0:
            course = canTake.pop()
            # print("current is %s" %course)
            totalFinished += 1
            if course in adjList:
                for neighbor in adjList[course]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        canTake.add(neighbor)
                    
        return totalFinished == numCourses
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
