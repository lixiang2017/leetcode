'''
DP
T: O(N^2)
S: O(N)

执行用时：36 ms, 在所有 Python3 提交中击败了86.61% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了25.00% 的用户
通过测试用例：20 / 20
'''
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        f = [0] + [1000 * n] * n
        for i in range(n):
            curWidth = maxHeight = 0
            for j in range(i, -1, -1):
                curWidth += books[j][0]
                if curWidth > shelfWidth:
                    break
                maxHeight = max(maxHeight, books[j][1])
                f[i + 1] = min(f[i + 1], f[j] + maxHeight)
        return f[n]


'''
DFS + cache

执行用时：44 ms, 在所有 Python3 提交中击败了41.96% 的用户
内存消耗：16.8 MB, 在所有 Python3 提交中击败了8.93% 的用户
通过测试用例：20 / 20
'''
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        @cache
        def f(i):
            if i == 0:
                return 0
            curWidth = maxHeight = 0
            res = 1000 * n
            for j in range(i, 0, -1):
                curWidth += books[j - 1][0]
                if curWidth > shelfWidth:
                    break
                maxHeight = max(maxHeight, books[j - 1][1])
                res = min(res, f(j - 1) + maxHeight)     
            return res

        return f(n)

