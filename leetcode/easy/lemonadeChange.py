class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveBill = tenBill = 0
        for bill in bills:
            if fiveBill < 0 or tenBill < 0:
                return False
            if bill == 5:
                fiveBill += 1
            elif bill == 10:
                fiveBill -= 1
                tenBill += 1
            else:
                if tenBill > 0:
                    tenBill -= 1
                    fiveBill -= 1
                else:
                    fiveBill -= 3
        return (fiveBill >= 0 and tenBill >= 0)
