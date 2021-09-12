'''
approach: Divide and Conquer (DFS) + Two Pointers + Hash Table
时间复杂度：O(N⋅Σ)，其中 N 为字符串的长度，Sigma Σ 为字符集的大小，本题中等于 26。
于每次递归调用都会完全去除某个字符，因此递归深度最多为 Sigma Σ。
空间复杂度：O(Sigma^2) = O(Σ^2)。递归的深度为 O(Sigma) = O(Σ)，每层递归需要开辟 O(Sigma) = O(Σ) 的额外空间。

ref:
https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/zhi-shao-you-kge-zhong-fu-zi-fu-de-zui-c-o6ww/

执行用时：28 ms, 在所有 Python 提交中击败了42.20%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了86.67%的用户
'''


from collections import Counter

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        N = len(s)
        return self.divideConquer(s, 0, N - 1, k)
    
    def divideConquer(self, s, left, right, k):
        longest = 0

        freq = Counter(s[left: right + 1])
        split = None
        for letter, cnt in freq.iteritems():
            if cnt < k:
                split = letter
                break
        
        if split is None:
            return right - left + 1
        
        i = left
        while i <= right:
            while i <= right and s[i] == split:
                i += 1
            if i > right:
                break
            start = i
            while i <= right and s[i] != split:
                i += 1

            length = self.divideConquer(s, start, i - 1, k)
            longest = max(longest, length)

        return longest


'''
copy from justyy, recursion

执行用时：48 ms, 在所有 Python3 提交中击败了29.38% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了10.99% 的用户
通过测试用例：35 / 35
'''
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        cnt = Counter(s)
        for ch, c in cnt.items():
            if c < k:
                return max(self.longestSubstring(x, k) for x in s.split(ch))

        return len(s)



'''
执行用时：60 ms, 在所有 Python3 提交中击败了20.24% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了77.48% 的用户
通过测试用例：35 / 35
'''
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        def divideConquer(l, r):
            if l >= r:
                return 0

            memo = Counter(s[l: r])
            splitter = None
            longest = 0
            for ch, cnt in memo.items():
                if cnt < k:
                    splitter = ch
                    break
            if not splitter:
                return r - l
            
            while l < r:
                while l < r and s[l] == splitter:
                    l += 1
                if l >= r:
                    break
                start = l
                while l < r and s[l] != splitter:
                    l += 1
                length = divideConquer(start, l)
                longest = max(length, longest)

            return longest
        
        return divideConquer(0, len(s))
