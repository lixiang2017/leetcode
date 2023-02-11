'''
heap

执行用时：44 ms, 在所有 Python3 提交中击败了26.67% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了47.27% 的用户
通过测试用例：280 / 280
'''
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        ans = 0
        h = [-x for x in amount if x != 0]
        heapify(h)
        while h:
            if len(h) > 1:
                x = heappop(h) + 1
                y = heappop(h) + 1
                if x:
                    heappush(h, x)
                if y:
                    heappush(h, y)
                ans += 1
            else:
                ans -= heappop(h)
        return ans 


'''
math

执行用时：36 ms, 在所有 Python3 提交中击败了69.70% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了91.51% 的用户
通过测试用例：280 / 280
'''
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        return max(max(amount), (sum(amount) + 1) >> 1)

'''
执行用时：24 ms, 在所有 Python3 提交中击败了99.39% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了88.48% 的用户
通过测试用例：280 / 280
'''
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        if amount[0] + amount[1] <= amount[2]:
            return amount[2]
        else:
            return (sum(amount) + 1) // 2


