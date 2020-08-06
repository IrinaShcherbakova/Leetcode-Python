class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seen = set()
        self.build_seq(tiles, 0, seen)
        return len(seen)
        
         
    def build_seq(self, tiles: str, index: int, seen: set) -> None:
        if index == len(tiles):
            return
        char = tiles[index]
        new = set()
        for seq in seen:
            for i in range(len(seq)+1):
                new_seq = seq[0:i] + char + seq[i:len(seq)]
                new.add(new_seq)
        new.add(char)
        seen.update(new)
        self.build_seq(tiles, index+1, seen)
        return
            
