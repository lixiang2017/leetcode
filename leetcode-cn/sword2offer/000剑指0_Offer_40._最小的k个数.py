'''
heap

执行用时：76 ms, 在所有 Python3 提交中击败了52.74% 的用户
内存消耗：16.8 MB, 在所有 Python3 提交中击败了22.06% 的用户
通过测试用例：38 / 38
'''
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        heapify(arr)
        return nsmallest(k, arr)

