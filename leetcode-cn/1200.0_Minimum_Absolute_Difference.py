'''
sort 

执行用时：92 ms, 在所有 Python3 提交中击败了97.86% 的用户
内存消耗：25.7 MB, 在所有 Python3 提交中击败了51.82% 的用户
通过测试用例：37 / 37
'''
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = arr[-1] - arr[0]
        ans = []
        for a, b in pairwise(arr):
            if b - a < min_diff:
                min_diff = b - a 
                ans = [[a, b]]
            elif b - a == min_diff:
                ans.append([a, b])
        return ans 
