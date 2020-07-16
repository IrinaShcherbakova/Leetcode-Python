class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = j = 0
        stack = []
        while i < len(pushed) or j < len(popped):
            if len(stack) == 0 or stack[-1] != popped[j]:
                if i == len(pushed):
                    return False
                stack.append(pushed[i])
                i += 1
            elif len(stack) > 0 and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            # print(stack)
        return i == len(pushed) and j == len(popped)
        
