class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        all_blue = 0
        max_bulb_turned = 0
        
        for i, bulb in enumerate(light):
            if max_bulb_turned < bulb:
                max_bulb_turned = bulb
            if max_bulb_turned == i + 1:
                all_blue += 1
  
        return all_blue
