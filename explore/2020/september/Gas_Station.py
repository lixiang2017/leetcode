'''
You are here!
Your runtime beats 79.07 % of python submissions.
'''


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(len(gas)):
        	total_tank = total_tank + gas[i] - cost[i]
        	curr_tank = curr_tank + gas[i] - cost[i]

        	if curr_tank < 0:
        		starting_station = i + 1
        		curr_tank = 0

        return starting_station if total_tank >= 0 else -1

if __name__ == '__main__':
	gas  = [1,2,3,4,5]
	cost = [3,4,5,1,2]
	assert Solution().canCompleteCircuit(gas, cost) == 3

	gas  = [2,3,4]
	cost = [3,4,3]
	assert Solution().canCompleteCircuit(gas, cost) == -1
