'''
wrong answer
'''


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        one_combination = []
        def check(mask, k, n):
            global one_combination
            # print one_combination
            one_combination = []

            for i in range(9):
            	if (1 << i) & mask:
            		one_combination.append(i + 1)

            return len(one_combination) == k and sum(one_combination) == n


        ans = []
        for mask in range(1 << 9):
            if check(mask, k, n):
                print mask
                print one_combination
                ans.append(one_combination)
        return ans

if __name__ == '__main__':
	k = 3
	n = 7
	print Solution().combinationSum3(k, n) # expect [[1,2,4]]

	k = 3
	n = 9
	print Solution().combinationSum3(k, n) # expect [[1,2,6], [1,3,5], [2,3,4]]


'''
output

11
[]
[[]]
14
[]
21
[]
35
[]
[[], [], []]
'''