'''
approach: hashmap / TwoSum
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 65.63 % of python submissions.
You are here!
Your memory usage beats 13.84 % of python submissions.
'''

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        twoSum = defaultdict(int)
        size = len(nums)
        operations = 0
        
        for i in range(size):
            if nums[i] in twoSum:
                operations += 1
                twoSum[nums[i]] -= 1
                if 0 == twoSum[nums[i]]:
                    del twoSum[nums[i]]
            else:
                twoSum[k - nums[i]] += 1
        
        return operations
            