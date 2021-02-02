'''
approach: hashmap + divide and conquer

You are here!
Your runtime beats 34.38 % of python submissions.

time: O(N ^ 2)
space: O(N ^ 2)
'''


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB = collections.Counter(a + b for a in A for b in B)
        return sum(AB[-c - d] for c in C for d in D)
    
