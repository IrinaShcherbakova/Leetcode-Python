class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        first = [0] * 26
        for char in A[0]:
            first[ord(char)-97] += 1
        for i in range(1, len(A)):
            temp = [0] * 26
            for char in A[i]:
                temp[ord(char)-97] += 1
            for j in range(len(first)):
                if first[j] == 0:
                    continue
                if temp[j] == 0 and first[j] > 0:
                    first[j] = 0
                else:
                    first[j] = min(first[j], temp[j])
        ans = ""
        for i in range(len(first)):
            char = chr(i + 97)
            ans = ans + (char*first[i])
        return ans
            
