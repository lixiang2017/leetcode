'''
You are here!
Your runtime beats 22.24 % of python submissions.
'''


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        def check(mask, k, n):
        	one_combination = []

        	for i in range(9):
        		if (1 << i) & mask:
        			one_combination.append(i + 1)

        	if len(one_combination) == k and sum(one_combination) == n:
        		return one_combination
        	else:
        		return None

        ans = []
        for mask in range(1 << 9):
        	one = check(mask, k, n)
        	if one:
        		ans.append(one)
       	return ans

if __name__ == '__main__':
	k = 3
	n = 7
	print Solution().combinationSum3(k, n) # [[1,2,4]]

	k = 3
	n = 9
	print Solution().combinationSum3(k, n) # [[1,2,6], [1,3,5], [2,3,4]]
