'''
执行用时：44 ms, 在所有 Python3 提交中击败了67.20% 的用户
内存消耗：19.4 MB, 在所有 Python3 提交中击败了5.11% 的用户
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = list(reversed(s))


'''
执行用时：32 ms, 在所有 Python3 提交中击败了97.25% 的用户
内存消耗：19.3 MB, 在所有 Python3 提交中击败了25.70% 的用户
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()



'''
Iteration
Two Pointers,T:O(N),S:O(1)
执行用时：28 ms, 在所有 Python3 提交中击败了99.24% 的用户
内存消耗：19.2 MB, 在所有 Python3 提交中击败了54.89% 的用户
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


'''
Recursion, DFS
T:O(N),S:O(N)
执行用时：52 ms, 在所有 Python3 提交中击败了37.04% 的用户
内存消耗：49 MB, 在所有 Python3 提交中击败了5.03% 的用户
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        def dfs(l, r):
            if l >= r:
                return
            s[l], s[r] = s[r], s[l]
            dfs(l + 1, r - 1)

        dfs(l, r)


'''
Runtime: 415 ms, faster than 7.13% of Python3 online submissions for Reverse String.
Memory Usage: 18.7 MB, less than 15.24% of Python3 online submissions for Reverse String.
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[:: -1]


'''
Runtime: 225 ms, faster than 71.60% of Python3 online submissions for Reverse String.
Memory Usage: 18.4 MB, less than 89.54% of Python3 online submissions for Reverse String.
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
