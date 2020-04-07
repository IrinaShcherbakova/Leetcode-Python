class Solution:
    def compress(self, chars: List[str]) -> int:
        slow = fast = length = 0
        while fast < len(chars):
            current = chars[fast]
            count = 0
            while fast < len(chars) and chars[fast] == current:
                fast += 1
                count += 1
            chars[slow] = current
            slow += 1
            if count == 1:
                length += 1
                continue
            #write count into array
            count = str(count)
            length = length + 1 + len(count)
            for ch in count:
                chars[slow] = ch
                slow += 1
        return length
