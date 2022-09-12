'''
Greedy + Sort
T: O(NlogN + N)
S: O(logN)

Runtime: 121 ms, faster than 11.32% of Python3 online submissions for Bag of Tokens.
Memory Usage: 13.9 MB, less than 99.06% of Python3 online submissions for Bag of Tokens.
'''
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = ans = 0
        tokens.sort()
        i, j = 0, len(tokens) - 1
        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                score += 1
                ans = max(ans, score)
                i += 1
            elif score > 0:
                score -= 1
                power += tokens[j]
                j -= 1
            else:
                break 
        return ans 
