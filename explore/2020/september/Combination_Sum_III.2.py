'''
You are here!
Your memory usage beats 99.80 % of python submissions.
'''

from copy import deepcopy

class Solution(object):

    one_combination = []
    def check(self, mask, k, n):
        global one_combination
        one_combination = []

        for i in range(9):
            if (1 << i) & mask:
                one_combination.append(i + 1)

        return len(one_combination) == k and sum(one_combination) == n


    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        for mask in range(1 << 9):
            if self.check(mask, k, n):
                # print mask
                # print one_combination
                ans.append(one_combination)
                # ans.append(deepcopy(one_combination))
        return ans


if __name__ == '__main__':
	k = 3
	n = 7
	print Solution().combinationSum3(k, n) # expect [[1,2,4]]

	k = 3
	n = 9
	print Solution().combinationSum3(k, n) # expect [[1,2,6], [1,3,5], [2,3,4]]

