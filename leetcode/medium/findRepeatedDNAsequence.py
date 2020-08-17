class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counts = {}
        for i in range(len(s) - 9):
            dna = s[i:i+10]
            if dna in counts:
                counts[dna] += 1
            else:
                counts[dna] = 1
        res = []
        for dna in counts:
            if counts[dna] > 1:
                res.append(dna)
        return res
                
