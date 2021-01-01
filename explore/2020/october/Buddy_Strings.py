'''
You are here!
Your runtime beats 87.31 % of python submissions.
'''



class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        
        set_A = set(A)
        set_B = set(B)
        if set_A != set_B:
            return False

        if A == B and len(set_A) < len(A):
            return True
        
        diff = [ord(a) - ord(b) for a, b in zip(A, B) if (ord(a) - ord(b)) != 0]
        if len(diff) == 2 and sum(diff) == 0:
            return True
        else:
            return False