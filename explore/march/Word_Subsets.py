'''
approach: Hash Table
Time: O(N * W + N * (W + S)) <= O(10000 * 10 + 10000 * (10 + 26)) = O(10000 * 46),
	where N is the number of words in A or B, 
	W is the length of every word, S the number of characters appear in B.
Space: O(S + W + W) <= O(26 + 10 + 10) = O(1), ignore the result of universals.

You are here!
Your memory usage beats 67.86 % of python submissions.
'''


class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        universals = []
        lowest = defaultdict(int)
        for b in B:
            lowb = defaultdict(int)
            for letter in b:
                lowb[letter] += 1
                if lowb[letter] > lowest[letter]:
                    lowest[letter] = lowb[letter]
        # print lowest
        for a in A:
            seen = defaultdict(int)
            universal = True
            for letter in a:
                seen[letter] += 1
            for letter, lowCnt in lowest.iteritems():
                if seen[letter] < lowCnt:
                    universal = False
                    break
            if universal:
                universals.append(a)
                
        return universals
                
            