'''
approach: prefixSum + suffixSum + hash(Two Sum)

Time: O(N * 2) = O(N)
Space: O(N * 3) = O(N)

You are here!
Your runtime beats 15.92 % of python submissions.
You are here!
Your memory usage beats 7.61 % of python submissions.
'''



class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        if nums[0] == x or nums[-1] == x: return 1
        
        size = len(nums)
        prefixSum = [0 for _ in range(size)]
        suffixSum = [0 for _ in range(size)]
        operations = []
        twoSum = defaultdict(int) # addend -> index
        twoSum[x] = -1
            
        for i in range(size):
            if i > 0:
                prefixSum[i] = prefixSum[i - 1]
            prefixSum[i] += nums[i]
            if x - prefixSum[i] > 0:
                twoSum[x - prefixSum[i]] = i
        
        for i in range(size - 1, -1 , -1):
            if i <= size - 2:
                suffixSum[i] = suffixSum[i + 1]
            suffixSum[i] += nums[i]
            if suffixSum[i] in twoSum and i > twoSum[suffixSum[i]]:
                # print twoSum[suffixSum[i]], i
                operations.append(twoSum[suffixSum[i]] + 1 + size - 1 - i + 1)
        
        # print 'operations: ', operations
        if operations:
            return min(operations)
        else:
            return -1
    