class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minAngle = minutes * 6
        hourAngle = (hour * 30 if hour != 12 else 0 * 30)
        hourHand = (0 if minutes == 0 else 30 / (60 / minutes))
        hourAngle += hourHand
        crossAngle = (360 - minAngle + hourAngle if minAngle > hourAngle else 360 - hourAngle + minAngle)
        normalAngle = abs(minAngle-hourAngle)
        return min(crossAngle, normalAngle)
