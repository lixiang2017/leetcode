'''
Sort

52 / 52 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 15.3 MB
提交时间：5 分钟前
'''
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i for _, i in sorted([(sum(row), i)  for i, row in enumerate(mat)])[: k]]

