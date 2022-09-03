'''
sort + DP
T: O(NlogN + N^2)
S: O(N)

执行用时：2212 ms, 在所有 Python3 提交中击败了13.70% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了19.30% 的用户
通过测试用例：205 / 205
'''
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        dp = [1] * n
        # i -> j
        for j in range(1, n):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)


'''
just return dp[-1]
T: O(NlogN + N^2 + N)
S: O(N)

执行用时：1972 ms, 在所有 Python3 提交中击败了40.54% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了14.48% 的用户
通过测试用例：205 / 205
'''
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        dp = [1] * n
        # i -> j
        for j in range(1, n):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)
        return dp[-1]


'''
sort + binary search
T: O(NlogN + NlogN)
S: O(N)

执行用时：84 ms, 在所有 Python3 提交中击败了52.70% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了78.76% 的用户
通过测试用例：205 / 205
'''
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        arr = []
        for x, y in pairs:
            i = bisect_left(arr, x)
            if i < len(arr):
                arr[i] = min(arr[i], y)
            else:
                arr.append(y)
        return len(arr)


'''
greedy + sort
sort + binary search
T: O(NlogN + N)
S: O(N)

执行用时：52 ms, 在所有 Python3 提交中击败了80.89% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了78.76% 的用户
通过测试用例：205 / 205
'''
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur, ans = -inf, 0
        for x, y in sorted(pairs, key=lambda p: p[1]):
            if cur < x:
                cur = y 
                ans += 1
        return ans 

