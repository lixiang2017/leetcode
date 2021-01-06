'''
appoach: Two Pointers
Time: O(N), the length of string s
Space: O(1) or O(N) if every group has exactly 3 characters.

执行结果：
通过
显示详情
执行用时：16 ms, 在所有 Python 提交中击败了96.83% 的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了79.37% 的用户
'''

class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        intervals = []
        size = len(s)
        i = 0
        while i < size:
            start = i
            start_letter = s[i]
            j = start + 1
            while j < size and s[j] == s[start]:
                j += 1
            # interval: [i, j - 1]
            if j - 1 - i >= 2:
                intervals.append([i, j - 1])
            
            # move to next
            i = j

        return intervals
        
