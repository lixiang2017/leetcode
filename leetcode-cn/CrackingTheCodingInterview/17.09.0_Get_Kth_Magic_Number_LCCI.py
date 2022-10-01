'''
heap

执行用时：24 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了97.57% 的用户
通过测试用例：20 / 20
'''
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        h = [1]
        seen = {1}
        while k > 1:
            x = heappop(h)
            for m in [3 * x, 5 * x, 7 * x]:
                if m not in seen:
                    seen.add(m)
                    heappush(h, m)
            k -= 1
        return heappop(h)
