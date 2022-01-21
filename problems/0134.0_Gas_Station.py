'''
Greedy
T: O(N)
S: O(1)

ref:
https://leetcode.com/problems/gas-station/discuss/42568/Share-some-of-my-ideas.

I have thought for a long time and got two ideas:

    If car starts at A and can not reach B. Any station between A and B
    can not reach B.(B is the first station that A can not reach.)
    If the total number of gas is bigger than the total number of cost. There must be a solution.
    (Should I prove them?)


Runtime: 739 ms, faster than 22.25% of Python3 online submissions for Gas Station.
Memory Usage: 18.8 MB, less than 75.25% of Python3 online submissions for Gas Station.
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = tank = 0
        for i, g in enumerate(gas):
            tank += g - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0

        return start
