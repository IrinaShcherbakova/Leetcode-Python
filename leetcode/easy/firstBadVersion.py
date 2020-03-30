# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        currentVersion = n // 2
        lastFalse = None
        while True:
            if currentVersion == 0:
                currentVersion += 1
            if isBadVersion(currentVersion):
                if currentVersion == 1 or currentVersion == n :
                    return currentVersion
                if not isBadVersion(currentVersion-1):
                    return currentVersion
                #go left to search for first bad version
                if lastFalse:
                    currentVersion = currentVersion - ((currentVersion - lastFalse) // 2)  
                else:
                    currentVersion = currentVersion // 2 
            else: #go right 
                lastFalse = currentVersion
                currentVersion = currentVersion + ((n + 1 - currentVersion) // 2)
