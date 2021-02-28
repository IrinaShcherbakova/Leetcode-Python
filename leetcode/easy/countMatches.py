class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        index = 0
        if ruleKey == 'color':
            index = 1
        if ruleKey == 'name':
            index = 2
        
        total = 0
        for item in items:
            if item[index] == ruleValue:
                total += 1
        
        return total
        
