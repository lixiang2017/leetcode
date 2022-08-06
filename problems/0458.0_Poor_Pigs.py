'''
k轮：k+1 进制

Runtime: 34 ms, faster than 87.59% of Python3 online submissions for Poor Pigs.
Memory Usage: 13.9 MB, less than 74.45% of Python3 online submissions for Poor Pigs.
'''
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        k = minutesToTest // minutesToDie + 1
        pig = 0
        while k ** pig < buckets:
            pig += 1
        return pig 
