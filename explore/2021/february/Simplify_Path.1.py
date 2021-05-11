'''
approach: Split + Dict

ref:
https://leetcode-cn.com/problems/simplify-path/solution/python-4-line-by-qqqun902025048/


Success
Details 
Runtime: 28 ms, faster than 27.37% of Python online submissions for Simplify Path.
Memory Usage: 13.7 MB, less than 38.68% of Python online submissions for Simplify Path.
'''



class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        parts = []
        for p in path.split('/'):
            parts = {'.': parts, '': parts, '..': parts[:-1]}.get(p, parts + [p])
        return '/' + '/'.join(parts)
