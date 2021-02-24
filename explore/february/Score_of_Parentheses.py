'''
approach: Divide and Conquer
Time: O(N ^ 2) ??? I don't know why.
Space: O(N)

ref:
https://leetcode-cn.com/problems/score-of-parentheses/solution/gua-hao-de-fen-shu-by-leetcode/

'''


class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        def balanced(i, j):
            # score of a balanced string S[i: j]
            score = bal = 0
            
            # split string into primitives
            for k in range(i, j):
                bal += 1 if S[k] == '(' else -1
                if bal == 0:
                    if k - i == 1:
                        score += 1
                    else:
                        score += 2 * balanced(i + 1, k)  # remove the outer cover
                    i = k + 1
              
            return score
        
        return balanced(0, len(S))


'''
approach: Stack
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 51.06 % of python submissions.
You are here!
Your memory usage beats 29.79 % of python submissions.
'''



class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = [0] # the score of current frame
        
        for x in S:
            if x == '(':
                stack.append(0)
            else:
                value = stack.pop()
                stack[-1] += max(2 * value, 1)
        
        return stack.pop()
    




'''
approach: Count Cores
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 51.06 % of python submissions
You are here!
Your memory usage beats 56.91 % of python submissions.
'''


class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        score = depth = 0
        
        for i, x in enumerate(S):
            if x == '(':
                depth += 1
            else:
                depth -= 1
                if S[i - 1] == '(':
                    score += 1 << depth
        
        return score
    

'''
You are here!
Your runtime beats 51.06 % of python submissions.

'''
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        return eval(S.replace(')(', ')+(').replace('()', '1').replace(')', ')*2'))
    
