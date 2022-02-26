'''
执行用时：32 ms, 在所有 Python3 提交中击败了78.60% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了70.53% 的用户
通过测试用例：93 / 93
'''
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1:
            return bits[0] == 0

        last_two = bits[-2: ] 
        if last_two == [0, 0]:
            return True
        elif last_two == [0, 1] or last_two == [1, 1]:
            return False
        # .....01111...110  # count 1
        ones = 0
        i = len(bits) - 2
        while i >= 0 and bits[i] == 1:
            ones += 1
            i -= 1
        return ones % 2 == 0
        