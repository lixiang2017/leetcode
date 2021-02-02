'''
approach: hashmap + divide and conquer

You are here!
Your runtime beats 80.63 % of python submissions.

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
        AB = defaultdict(int)
        count = 0
        for a in A:
            for b in B:
                if a + b in AB:
                    AB[a + b] += 1
                else:
                    AB[a + b] = 1
        
        for c in C:
            for d in D:
                if -(c + d) in AB:
                    count += AB[-(c + d)]
        return count
