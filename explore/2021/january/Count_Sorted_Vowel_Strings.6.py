'''
approach: DP / Iteration
Time: O(N)
Space: O(1)

ref:
https://leetcode-cn.com/problems/count-sorted-vowel-strings/solution/shu-xue-fang-fa-shuang-bai-by-avery_/

You are here!
Your runtime beats 60.96 % of python submissions.
You are here!
Your memory usage beats 71.23 % of python submissions.
'''

class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = e = i = o = u = 1
        
        for _ in range(n):
            a = a + e + i + o + u
            e = e + i + o + u
            i = i + o + u
            o = o + u
        
        return a
