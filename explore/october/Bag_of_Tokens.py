'''
two pointers

You are here!
Your runtime beats 96.43 % of python submissions.
'''

class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens.sort()
        if not tokens or P < tokens[0]:
            return 0
        
        score = 0
        max_score = 0
        l, r = 0, len(tokens) - 1
        while l <= r:
            if P >= tokens[l]:
                P -= tokens[l]
                l += 1
                score +=1
            else:
                if score > 0:
                    score -= 1
                    P += tokens[r]
                    r -= 1
            max_score = max(score, max_score)
        return max_score
        