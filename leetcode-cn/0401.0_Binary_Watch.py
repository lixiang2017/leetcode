'''

执行用时：44 ms, 在所有 Python3 提交中击败了58.99%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了5.22%的用户
'''

from itertools import combinations

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        possible = []
        for turnedHour in range(turnedOn + 1):
            turnedMinute = turnedOn - turnedHour
            com_hours = self.combinationsHour(turnedHour)
            com_minutes = self.combinationsMinute(turnedMinute)
            if not com_hours or not com_minutes:
                continue
            for h in com_hours:
                for m in com_minutes:
                    possible.append(h + ':' + m)

        return possible
        
    def combinationsHour(self, turnedHour):
        if 0 == turnedHour:
            return ['0']
        if turnedHour > 4:
            return []
        
        choices = [1, 2, 4, 8]
        # coms = list(combinations(choices, turnedHour))
        coms = combinations(choices, turnedHour)
        return [str(sum(com)) for com in coms if sum(com) <= 11]
    
    def combinationsMinute(self, turnedMinute):
        if 0 == turnedMinute:
            return ['00']
        if turnedMinute >= 6:
            return []
        
        choices = [1, 2, 4, 8, 16, 32]
        coms = combinations(choices, turnedMinute)
        # return [str(sum(com)) if len(str(sum(com))) == 2 else '0' + str(sum(com)) if len for com in coms if sum(com) <= 59]
        combines = []
        for com in coms:
            total = sum(com)
            if total > 59:
                continue
            if 2 == len(str(total)):
                combines.append(str(total))
            else:
                combines.append('0' + str(total))
                      
        return combines

