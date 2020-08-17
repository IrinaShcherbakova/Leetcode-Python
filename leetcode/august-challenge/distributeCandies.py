class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        count = 1
        sumCandies = 0
        i = 0
        while count + sumCandies < candies:
            if i == num_people:
                i = 0
            res[i] += count
            sumCandies += count
            # print(sumCandies)
            count += 1
            i += 1
        if i == num_people:
            i = 0
        res[i] += candies - sumCandies
        return res
