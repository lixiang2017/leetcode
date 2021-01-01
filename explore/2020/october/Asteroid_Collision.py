'''
You are here!
Your runtime beats 58.42 % of python submissions
'''

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stable = []
        
        for aster in asteroids:
            continue_flag = False
            if len(stable) > 0 and stable[-1] * aster < 0 and stable[-1] > 0 and aster < 0:
                while len(stable) > 0 and stable[-1] > 0 and aster < 0:
                    if stable[-1] > -aster:
                        # aster will disappear
                        break
                    elif stable[-1] == -aster:
                        # the top one in stack and aster disappear at the same time
                        stable.pop()
                        continue_flag = True
                        break
                    else: # stable[-1] < -aster
                        stable.pop()
                if continue_flag:
                    continue
                if len(stable) == 0 or stable[-1] < 0 and aster < 0:
                    stable.append(aster)
            else:
                stable.append(aster)
        
        return stable