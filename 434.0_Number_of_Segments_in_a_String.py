#! /usr/bin/python
"""
Author: lixiang
Success
Details 
Runtime: 8 ms, faster than 98.05% of Python online submissions for Number of Segments in a String.
Memory Usage: 11.7 MB, less than 87.23% of Python online submissions for Number of Segments in a String.
"""

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())

if __name__ == '__main__':
    s = "Hello, my name is John"
    assert Solution().countSegments(s) == 5