'''
approach: Hash Tables + Sort

You are here!
Your runtime beats 8.03 % of python submissions.
You are here!
Your memory usage beats 95.44 % of python submissions.
'''


class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order2real = {o: chr(ord('a') + i) for i, o in enumerate(order)}
        real2order = {chr(ord('a') + i): o for i, o in enumerate(order)}
        reals = []
        for word in words:
            reals.append(''.join([order2real[o] for o in word]))
        
        reals.sort()
        rewords = []
        for real in reals:
            rewords.append(''.join([real2order[r] for r in real]))
    
        return rewords == words