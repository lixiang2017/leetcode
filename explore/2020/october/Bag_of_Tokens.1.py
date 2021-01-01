'''
recursive

You are here!
Your runtime beats 76.79 % of python submissions.
'''

class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens.sort()
        
        def helper(tokens, P, low, high, score):
            if low > high:
                return score
            
            max_score = score
            if P >= tokens[low]:
                max_score = max(max_score, helper(tokens, P - tokens[low], low + 1, high, score + 1))
            elif score > 0:
                max_score = max(max_score, helper(tokens, P + tokens[high], low, high - 1, score - 1))
            
            return max_score

        return helper(tokens, P, 0, len(tokens) - 1, 0)
    