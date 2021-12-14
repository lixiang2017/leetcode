'''
binary search + presum + two pointers

执行用时：328 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：45 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：194 / 194
'''
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        presum = list(accumulate([f[1] for f in fruits], initial = 0))
        ans = 0
        # to left
        idxll = bisect_left(fruits, [startPos - k, 0])   # include idxll => idxll-1, idxll in presum
        idxlr = bisect_right(fruits, [startPos, float('inf')])  # include idxlr-1 => idxlr in presum
        ans = max(ans, presum[idxlr] - presum[idxll])
        # to right
        idxrl = bisect_left(fruits, [startPos, 0])   # include idxrl => idxrl-1, idxrl in presum
        idxrr = bisect_right(fruits, [startPos + k, float('inf')]) # include idxrr-1 => idxrr in presum
        ans = max(ans, presum[idxrr] - presum[idxrl])
        # two pointers, from leftmost to right, i --> j
        i, j = idxll, idxll
        while i < n and fruits[i][0] <= startPos:
            while j < n and fruits[j][0] - fruits[i][0] + (startPos - fruits[i][0]) <= k:
                # i->j, i+1 -> j+1, presum[j + 1] - presum[i]
                ans = max(ans, presum[j + 1] - presum[i])
                j += 1
            i += 1
        # two pointers, from rightmost to left, i --> j
        i, j = idxrr - 1, idxrr - 1     
        while j >= 0 and fruits[j][0] >= startPos:
            while i >= 0 and fruits[j][0] - fruits[i][0] + (fruits[j][0] - startPos) <= k:
                ans = max(ans, presum[j + 1] - presum[i])
                i -= 1
            j -= 1
        return ans
