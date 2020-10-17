class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dna = {}
        for i in range(len(s)-9):
            sequence = s[i:i+10]
            if sequence in dna:
                dna[sequence] += 1
            else:
                dna[sequence] = 1
        res = []
        for sequence in dna:
            if dna[sequence] > 1:
                res.append(sequence)
        return res
