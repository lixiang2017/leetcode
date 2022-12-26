'''
heap

执行用时：392 ms, 在所有 Python3 提交中击败了18.90% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了63.78% 的用户
通过测试用例：96 / 96
'''
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        h = [-a, -b, -c]
        heapify(h)
        ans = 0
        while len(h) > 1:
            x, y = heappop(h), heappop(h)
            x += 1
            y += 1
            ans += 1
            if x != 0:
                heappush(h, x)
            if y != 0:
                heappush(h, y)
        return ans 

'''
sort 

执行用时：40 ms, 在所有 Python3 提交中击败了62.99% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了88.19% 的用户
通过测试用例：96 / 96
'''
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c])
        if a + b <= c:
            return a + b 
        return (a + b + c) // 2

'''
no sort

执行用时：32 ms, 在所有 Python3 提交中击败了93.70% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了98.43% 的用户
通过测试用例：96 / 96
'''
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        if a + b <= c:
            return a + b 
        elif a + c <= b:
            return a + c
        elif b + c <= a:
            return b + c
        return (a + b + c) // 2
