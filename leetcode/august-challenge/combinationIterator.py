class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.strings = []
        self.combine(characters, 0, combinationLength, "", self.strings)
        self.index = 0

    def next(self) -> str:
        res = self.strings[self.index]
        self.index += 1
        return res

    def hasNext(self) -> bool:
        return self.index < len(self.strings)
        
    
    def combine(self, characters: str, index: str, length: int, cur: str, res: List[str]) -> None:
        if len(cur) == length:
            res.append(cur)
            return
        if index == len(characters):
            return
        with_cur_index = cur + characters[index]
        without_cur_index = cur
        self.combine(characters, index+1, length, with_cur_index, res)
        self.combine(characters, index+1, length, without_cur_index, res)
        return
            
        
        
    
# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
