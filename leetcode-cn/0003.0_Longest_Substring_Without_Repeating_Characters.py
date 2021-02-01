'''
approach: (Hash Table / Set) + (Two Pointers / Sliding Window)
Time: O(N)
Space: O(longest)

执行结果：
通过
显示详情
执行用时：40 ms, 在所有 Python 提交中击败了96.02%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了86.47%的用户
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        size = len(s)
        i = j = 0
        # seen = {}
        seen = set()
        while i < size and j < size:
            if s[j] not in seen:
                seen.add(s[j])
                longest = max(longest, j - i + 1)
                j += 1
            else:
                seen.remove(s[i])
                i += 1

        return longest
