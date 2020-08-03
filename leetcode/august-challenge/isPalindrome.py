class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        # print(s)
        while left < right:
            # print("left: %s" %s[left])
            # print("right: %s" %s[right])
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
            
