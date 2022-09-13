'''
sort

执行用时：40 ms, 在所有 Python3 提交中击败了68.37% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了41.86% 的用户
通过测试用例：50 / 50
'''
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        five = len(arr) // 20
        arr.sort()
        return sum(arr[five: -five]) / (len(arr) - five - five)
