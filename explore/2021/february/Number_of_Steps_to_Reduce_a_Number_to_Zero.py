'''
approach: Bit Manipulation
Time: O(logN)
Space: O(1)

You are here!
Your runtime beats 50.17 % of python submissions.
You are here!
Your memory usage beats 99.11 % of python submissions.
'''


class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num:
            if num & 1:
                steps += 1
                num -= 1
            else:
                steps += 1
                num >>=1 
        
        return steps



class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num:
            num = (num - 1) if num & 1 else (num // 2)
            steps +=1 
        return steps
        