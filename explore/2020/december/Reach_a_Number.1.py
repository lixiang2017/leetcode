'''
approach: mathemetical

tricks:
1. the answers for target is the same as abs(target).
2. if the diff(steps - target) is even, just minus diff/2 instead of add diff/2 (diff/2-th step)
3. if the diff is odd, we need to move one more step(add step + 1), and check whether (step + 1) is odd or even.
 3.1 if step + 1 is odd, we can make it within step+1 steps.
 3.2 else we need one more step. 
    we can split [diff + (step + 1) + (step + 2)] / 2 into many parts, i.e. minus many diff/2 like trick-2.
    for example, if target is 23. 
    1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
    diff = 5, step + 1 = 8, step + 2 will be 9.
    (5 + 8 + 9) / 2 = 11, and 11 => 2 + 4 + 5, so we can reverse 2-nd, 4-th, 5-th step to reach the goal.

# ref
https://www.cnblogs.com/grandyang/p/8456022.html
https://leetcode.com/problems/reach-a-number/solution/

You are here!
Your runtime beats 83.33 % of python submissions.
'''


class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        
        step = steps = 0
        while steps < target:
            step += 1
            steps += step
        
        # print step, steps, target
        if steps == target:
            return step

        diff = steps - target
        if diff % 2 == 0:
            return step
        elif (step + 1) % 2 == 1:
            return step + 1
        else:
            return step + 2
        
'''
Your input

23

Your answer

9

Expected answer

9
'''     
