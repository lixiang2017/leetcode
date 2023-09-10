'''
32ms 击败 98.87%使用 Python3 的用户
15.42MB 击败 98.31%使用 Python3 的用户
'''
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24

