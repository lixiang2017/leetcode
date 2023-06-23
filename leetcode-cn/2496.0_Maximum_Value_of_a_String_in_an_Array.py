'''
执行用时：56 ms, 在所有 Python3 提交中击败了7.58% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了26.07% 的用户
通过测试用例：64 / 64
'''
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max(int(s) if all(ch.isdigit() for ch in s) else len(s) for s in strs)

