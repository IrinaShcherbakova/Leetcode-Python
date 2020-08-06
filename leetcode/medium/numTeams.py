class Solution:
    def numTeams(self, rating: List[int]) -> int:
        return self.recurse(rating, [], 0)
    
    
    def recurse(self, rating: List[int], team: List[int], index: int) -> int:
        total = 0
        if index == len(rating):
            return total
        for i in range(index, len(rating)):
            team.append(rating[i])
            if self.valid_team(team):
                total += 1
            elif len(team) < 3:
                total += self.recurse(rating, team, i+1)
            team.pop()
        return total
                
              
    def valid_team(self, team: List[int]) -> bool:
        if len(team) != 3:
            return False
        if team[0] > team[1]:
            return team[1] > team[2]
        if team[0] < team[1]:
            return team[1] < team[2]
        return False
