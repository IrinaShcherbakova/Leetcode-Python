class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        counts = [0]*26
        for task in tasks:
            index = ord(task) - 65
            counts[index] += 1
        counts.sort()
        units = len(tasks)
        mostFreq = counts.pop()
        cooldown = (mostFreq-1)*n
        numberOfSlots = mostFreq - 1
        print(counts)
        for i in range(len(counts)-1, -1, -1):
            cooldown -= min(counts[i], numberOfSlots)
            # print("cooldown is %s" %cooldown)
        return (units + cooldown) if cooldown > 0 else units
                
            
        
