class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        required_courses = [None] * n
        dependant_courses = [None] * n
        for pair in prerequisites:
            self.update_dependencies(required_courses, dependant_courses, pair[0], pair[1])
        ans = []
        
        print(required_courses)
        
        for pair in queries:
            prereq, course = pair[0], pair[1]
            if required_courses[course] and prereq in required_courses[course]:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
    
    
    # second depends on first
    def update_dependencies(self, required_courses: List[set], dependant_courses: List[set], first: int, second: int) -> None:
        if not dependant_courses[first]:
            dependant_courses[first] = set()
        dependant_courses[first].add(second)
        
        # propagate first as prerequisite
        stack = {second}
        while stack:
            cur = stack.pop()
            if not required_courses[cur]:
                required_courses[cur] = set()
            required_courses[cur].add(first)
            if required_courses[first]:
                required_courses[cur] = required_courses[cur].union(required_courses[first])
            if dependant_courses[cur]:
                stack = stack.union(dependant_courses[cur])                 
        return
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
