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
