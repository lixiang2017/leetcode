'''
执行用时：904 ms, 在所有 Python3 提交中击败了47.52% 的用户
内存消耗：70.7 MB, 在所有 Python3 提交中击败了31.21% 的用户
通过测试用例：59 / 59
'''
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        fraction = [(arr[i] / arr[j], arr[i], arr[j]) for i in range(n - 1) for j in range(i + 1, n)]
        return sorted(fraction)[k - 1][1: ]
        