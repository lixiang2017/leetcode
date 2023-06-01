'''
binary search
T: O(NlogN) + O(log(max_price_diff) * N)
S: O(1)

执行用时：996 ms, 在所有 Python3 提交中击败了26.40% 的用户
内存消耗：27.7 MB, 在所有 Python3 提交中击败了14.40% 的用户
通过测试用例：40 / 40
'''
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        l, r = 0, price[-1] - price[0]
        n = len(price)

        def check(m):
            prev = price[0]
            cnt = 1
            for i, p in enumerate(price):
                if i > 0 and p - prev >= m:
                    cnt += 1
                    prev = p 
            return cnt >= k

        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l - 1
