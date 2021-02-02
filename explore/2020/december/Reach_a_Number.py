'''
31 / 73 test cases passed.
    Status: Time Limit Exceeded
    
Submitted: 0 minutes ago
Last executed input: -1000000000
'''


class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        steps = defaultdict(set)
        steps[0] = set([0])

        idx = 0
        while True:
            for item in steps[idx]:
                if target == item + idx + 1 or target == item - idx - 1:
                    return idx + 1
                steps[idx + 1].add(item + idx + 1)
                steps[idx + 1].add(item - idx - 1)
            idx += 1        
