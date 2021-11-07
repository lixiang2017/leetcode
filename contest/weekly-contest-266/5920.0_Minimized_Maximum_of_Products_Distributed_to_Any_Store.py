'''
binary search
T: O(NlogN)
S: O(1)

执行用时：1340 ms, 在所有 Python3 提交中击败了33.33% 的用户
内存消耗：25.3 MB, 在所有 Python3 提交中击败了66.67% 的用户
通过测试用例：219 / 219
'''
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)
        ans = r
        while l <= r:
            mid = (l + r) // 2
            store = 0
            for q in quantities:
                need, remainder = divmod(q, mid)
                if remainder == 0:
                    store += need
                else:
                    store += need + 1
            if store <= n:
                # speed too less stores, lower its max
                ans = mid
                r = mid - 1
            else:
                # speed much more stores, higher its max
                l = mid + 1
        return ans


'''
need = (q + mid - 1) // mid
binary search
T: O(NlogN)
S: O(1)

执行用时：892 ms, 在所有 Python3 提交中击败了66.67% 的用户
内存消耗：25.1 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：219 / 219
'''
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)
        ans = r
        while l <= r:
            mid = (l + r) // 2
            store = 0
            for q in quantities:
                need = (q + mid - 1) // mid
                store += need
                
            if store <= n:
                # speed too less stores, lower its max
                ans = mid
                r = mid - 1
            else:
                # speed much more stores, higher its max
                l = mid + 1
        return ans

