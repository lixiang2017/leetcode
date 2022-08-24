'''
执行用时：40 ms, 在所有 Python3 提交中击败了70.87% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了5.65% 的用户
通过测试用例：106 / 106
'''
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)

'''
执行用时：40 ms, 在所有 Python3 提交中击败了70.87% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了9.57% 的用户
通过测试用例：106 / 106
'''
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
        