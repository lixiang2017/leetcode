'''
执行用时：48 ms, 在所有 Python3 提交中击败了8.30% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了88.24% 的用户
通过测试用例：111 / 111
'''
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(s <= queryTime <= e for s, e in zip(startTime, endTime))
        