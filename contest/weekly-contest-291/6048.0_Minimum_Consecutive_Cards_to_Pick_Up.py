'''
执行用时：132 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：33.3 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：78 / 78
'''
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = 100006
        pos = dict()
        for i, c in enumerate(cards):
            if c in pos:
                p = pos[c]
                ans = min(ans, i - p + 1)
            pos[c] = i
            
        return ans if ans != 100006 else -1


'''
执行用时：136 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：33.2 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：78 / 78
'''
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = -1
        pos = dict()
        for i, c in enumerate(cards):
            if c in pos:
                p = pos[c]
                if ans == -1 or ans > i - p + 1:
                    ans = i - p + 1
            pos[c] = i
            
        return ans

        