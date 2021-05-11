'''
BIT: Binary Indexed Tree / fenwick tree

65 / 65 test cases passed.
Status: Accepted
Runtime: 4848 ms
Memory Usage: 26 MB
Submitted: 0 minutes ago

You are here!
Your memory usage beats 37.50 % of python submissions.
'''

MOD = 10 ** 9 + 7

class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        n = max(instructions) + 1
        nums = [0 for _ in range(n)]

        def add(x):
            while x < n:
                nums[x] += 1
                x += self.lowbit(x)
        
        def getCost(x):
            # count for less than or equal to x
            cost = 0
            while x > 0:
                cost += nums[x]
                x -= self.lowbit(x)
            return cost
        
        total_cost = 0
        numsLength = 0
        
        for instr in instructions:
            # less than instr
            less = getCost(instr - 1)
            # greater than instr
            greater = numsLength - getCost(instr)
            total_cost += min(less, greater)
            total_cost %= MOD
            add(instr)
            numsLength += 1
        
        return total_cost
        
    
    
    def lowbit(self, x):
        return x & -x
