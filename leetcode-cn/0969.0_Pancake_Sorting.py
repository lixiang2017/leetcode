'''
执行用时：36 ms, 在所有 Python3 提交中击败了78.30% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了63.68% 的用户
通过测试用例：215 / 215
'''
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []
        while n:
            idx = arr.index(n)
            ans.append(idx + 1)
            arr = arr[: idx + 1][:: -1] + arr[idx + 1: ]
            ans.append(n)
            arr = arr[: n][:: -1] + arr[n :]
            n -= 1
        return ans

