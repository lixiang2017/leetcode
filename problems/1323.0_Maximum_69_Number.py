'''
Runtime: 58 ms, faster than 41.91% of Python3 online submissions for Maximum 69 Number.
Memory Usage: 13.9 MB, less than 54.69% of Python3 online submissions for Maximum 69 Number.
'''
class Solution:
    def maximum69Number (self, num: int) -> int:
        for m in [1000, 100, 10, 1]:
            if (num // m) % 10 == 6:
                return num + m * 3
        return num
        
        