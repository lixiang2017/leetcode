'''
approach: math -- permutation and combination

a + e + i + o + u = n, and a, e, i, o, u are not negative integers.

You are here!
Your runtime beats 28.42 % of python submissions.
You are here!
Your memory usage beats 21.92 % of python submissions.
'''


class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) / 24



class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        # The trick here is to recognize that the number of strings created follows the
        # pattern of the pantatope numbers. These numbers are in the fifth cell of any 
        # row in Pascal's triangle starting with the 5-term row of 1 4 6 4 1. Just like the 
        # number of strings that follows the rule given by the question, the pentatope 
        # numbers begin with 1, 5, 15, 35, 70, 126...
        #
        # The equation to find P_n is as follows:
        # (n(n + 1)(n + 2)(n + 3)) / 4! 
        # 
        # note 4! = 24
        n += 1 # to account for indexing differences b/w our pattern and the pentatope numbers 
        answer = (n*(n + 1)*(n + 2)*(n + 3)) / 24 
        return answer




class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        return len(list(itertools.combinations_with_replacement("aeiou",n)))