'''
You are here!
Your runtime beats 75.99 % of python submissions.
'''

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        ans = []
        
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                break   # contain ans[-1] > -new
            else:    # else statement won't be executed if break
                ans.append(new)
        
        return ans