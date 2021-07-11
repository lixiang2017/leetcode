'''
Sort and one more loop
Time: O(NlogN + N)
Space: O(1)

执行用时：28 ms, 在所有 Python3 提交中击败了98.91% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了85.56% 的用户
'''

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        N = len(citations)
        h = 0
        for i in range(N):
            if citations[i] >= i + 1:
                h = i + 1
                continue
            else:
                break

        return h
