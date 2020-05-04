"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        for employee in employees:
            if employee.id == id:
                subordinates = employee.subordinates
                importance = employee.importance
                for subordinate in subordinates:
                    importance += self.getImportance(employees, subordinate)
                return importance
        return 0

