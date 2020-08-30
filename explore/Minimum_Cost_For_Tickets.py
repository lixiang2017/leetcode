'''
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3436/
You are here!
Your runtime beats 41.16 % of python submissions.
'''


class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
       	dp = [float('inf')] * 366
       	dp[0] = 0
       	for day in days:
       		dp[day] = 0

       	for i in range(1, 366):
       		if dp[i] == float('inf'):
       			dp[i] = dp[i - 1]
       		else:
       			current = dp[i - 1] + costs[0]
       			current = min(dp[max(0, i - 7)] + costs[1], current)
       			current = min(dp[max(0, i - 30)] + costs[2], current)
       			dp[i] = current
       	return dp[days[-1]]
        

if __name__ == '__main__':
	days = [1,4,6,7,8,20]
	costs = [2,7,15]
	assert Solution().mincostTickets(days, costs) == 11

	days = [1,2,3,4,5,6,7,8,9,10,30,31]
	costs = [2,7,15]
	assert Solution().mincostTickets(days, costs) == 17