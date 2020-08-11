class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        deleted_once = False
        while left < right:
            # print("left: %s, right: %s" %(s[left],s[right]))
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif left+1 == right: 
                return (True if not deleted_once else False)
            elif deleted_once:
                return False
            else:
                deleted_once = True
                new_left = (left+1 if s[left+1] == s[right] and s[left+2] == s[right-1] else left)
                if left == new_left:
                    new_right = (right-1 if s[right-1] == s[left] and s[right-2] == s[left+1] else right)
                    if right == new_right:
                        return False
                    right = new_right
                else:
                    left = new_left
        return True
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
                
