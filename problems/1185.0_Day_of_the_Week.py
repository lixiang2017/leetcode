'''
Success
Details
Runtime: 16 ms, faster than 70.13% of Python online submissions for Day of the Week.
Memory Usage: 13.3 MB, less than 13.64% of Python online submissions for Day of the Week.
'''

class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        isleap = lambda y: y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)
        dayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        #              1    2   3   4   5  6   7   8   9   10  11  12
        daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # 20, 10, 2020  Tuesday
        
        # day since 31, 21, 1970
        def daysSinceStart(day, month, year):
            numDays = 0
            # year
            for y in range(year - 1, 1970, -1):
                numDays += 365 #  + 1 if isleap(y) else 0   # Wrong Answer, if False not add 365 as well
                numDays += 1 if isleap(y) else 0
                #if isleap(y):
                #    numDays += 1
            # month
            numDays += sum(daysInMonth[: month - 1])
            if month > 2:
                numDays +=  1 if isleap(year) else 0
                #if isleap(year):
                #    numDays += 1
            # day
            numDays += day
            return numDays
        
        knownStart = daysSinceStart(20, 10, 2020)
        days = daysSinceStart(day, month, year)
        return dayNames[(days - knownStart + 2) % 7] 