class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        daysPerMonth = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
        commonYear = 365
        leapYear = 366
        startYear = 1971
        startMonth = 1
        weekDays = {1 : "Friday", 2 : "Saturday", 3 : "Sunday", 4 : "Monday", 5 : "Tuesday", 6 : "Wednesday", 0 : "Thursday"}
        totalDays = 0
        while startYear < year:
            if self.isLeap(startYear):
                totalDays += leapYear
            else:
                totalDays += commonYear
            startYear += 1
        while startMonth < month:
            if self.isLeap(year) and startMonth == 2:
                totalDays = totalDays + daysPerMonth[startMonth] + 1
            else:
                totalDays = totalDays + daysPerMonth[startMonth]
            startMonth += 1
        totalDays += day
        return weekDays[totalDays % 7]
    
    
    def isLeap(self, year: int) -> bool:
        if year % 4 != 0:
            return False
        if year % 100 != 0:
            return True
        if year % 400 != 0:
            return False
        return True
        
     
