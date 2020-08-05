class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        res = []
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        count = 0
        for num in sorted(counts, key=counts.get, reverse=True):
            res.append(num)
            count += 1
            if count == k:
                return res
        return res
               class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = {}
        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
        
        groups_with_same_freq = {}
        for word in frequency:
            freq = frequency[word] 
            if freq in groups_with_same_freq:
                groups_with_same_freq[freq].append(word)
            else:
                groups_with_same_freq[freq] = [word]
                
        count = 0
        res = []
        for freq in sorted(groups_with_same_freq, reverse = True):
            words = groups_with_same_freq[freq]
            words.sort()
            if count + len(words) < k:
                res += words
                count += len(words)
            else:
                res += words[:k-count]
                return res
        return res
            
        
             
