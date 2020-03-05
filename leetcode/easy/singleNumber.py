def singleNumber(self, nums: List[int]) -> int:
    numbers = []
    for number in nums:
        if number not in numbers:
            numbers.append(number)
        else:
            numbers.remove(number)
    return numbers[0]