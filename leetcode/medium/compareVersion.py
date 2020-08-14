class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        one = self.read_version(version1)
        two = self.read_version(version2)
        if len(one) < len(two):
            self.pad_zeros(one, len(two)-len(one))
        elif len(one) > len(two):
            self.pad_zeros(two, len(one)-len(two))
        i = 0
        while i < len(one) and i < len(two):
            if one[i] > two[i]:
                return 1
            elif one[i] < two[i]:
                return -1
            else:
                i += 1
        return 0
    
    
    def read_version(self, version: str) -> List[int]:
        levels = []
        index = 0
        while index < len(version):
            index, level = self.read_level(index, version)
            levels.append(level)
        return levels
        
    
    # returns next index and version of the level starting from index
    def read_level(self, index: int, version: str) -> tuple:
        start = index
        while index < len(version) and version[index] != '.':
            index += 1
        # skip leading zero's
        while start < index and version[start] == '0':
            start += 1
        level = (version[start:index] if start < index else '0')
        index += 1 # skip dot
        return index, int(level)
    
    
    def pad_zeros(self, arr: List[int], num_zeros: int) -> None:
        for i in range(num_zeros):
            arr.append(0)
        return arr
    
    
    
    
    
    
    
    
            
            
            
