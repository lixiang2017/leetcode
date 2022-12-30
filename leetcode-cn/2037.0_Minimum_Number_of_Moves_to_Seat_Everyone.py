'''
执行用时：40 ms, 在所有 Python3 提交中击败了60.12% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了65.90% 的用户
通过测试用例：262 / 262
'''
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(a - b) for a, b in zip(sorted(seats), sorted(students)))
        