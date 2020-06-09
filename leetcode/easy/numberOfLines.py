class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        fullLineCounter = 0
        spaceLeft = 100
        for char in S:
            charWidth = widths[ord(char)-97]
            #print(charWidth)
            if charWidth <= spaceLeft:
                spaceLeft -= charWidth
                #print(spaceLeft)
            else:
                fullLineCounter += 1
                spaceLeft = 100 - charWidth
        return [fullLineCounter+1, 100-spaceLeft]
