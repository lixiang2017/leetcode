'''
compact arrays first

You are here!
Your runtime beats 92.81 % of python submissions.
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
        A = self.compact(A)
        B = self.compact(B)
        C = self.compact(C)
        D = self.compact(D)
        count = 0
        AB = {}
        for ak, av in A.iteritems():
            for bk, bv in B.iteritems():
                if ak + bk in AB:
                    AB[ak + bk] += av * bv
                else:
                    AB[ak + bk] = av * bv
        
        for ck, cv in C.iteritems():
            for dk, dv in D.iteritems():
                if -(ck + dk) in AB:
                    count += AB[-(ck + dk)] * cv * dv
        
        
        return count
    
    def compact(self, arr):
        return collections.Counter(arr)
        