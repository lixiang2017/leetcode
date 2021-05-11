'''
approach: Iteration

You are here!
Your runtime beats 44.26 % of python submissions.
You are here!
Your memory usage beats 40.38 % of python submissions.
'''


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        N = len(digits)
        if 0 == N:
            return []
        
        possibilites = ['']
        digit2letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        idx = 0
        while idx < N:
            coms = []
            for poss in possibilites:
                for letter in digit2letters[int(digits[idx])]:
                    coms.append(poss + letter)

            possibilites = coms[:]
            idx += 1

        return possibilites
