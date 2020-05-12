
class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = []
        for char in address:
            if char == '.':
                result.append("[")
                result.append(".")
                result.append("]")
            else:
                result.append(char)
        return ''.join(result)
