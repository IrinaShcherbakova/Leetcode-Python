class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        i = 0
        while i < len(S):
            if len(stack) > 0 and stack[-1] == S[i]:
                while len(stack) > 0 and stack[-1] == S[i]:
                    stack.pop()
                i += 1
                continue
            if i+1 < len(S) and S[i] == S[i+1]:
                i += 2
            else:
                stack.append(S[i])
                i += 1
        ans = ""
        for char in stack:
            ans += char
        return ans
            
