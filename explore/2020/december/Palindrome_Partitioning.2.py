'''
You are here!
Your runtime beats 5.99 % of python submissions.
'''


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        def helper(arr, substring):
            if substring:
                # do
                for i in range(1, len(substring) + 1):
                    if substring[:i] == substring[:i][:: -1]:
                        helper(arr + [substring[:i]], substring[i:])
            elif arr:
                res.append(arr)
            
        helper([], s)
        return res
    