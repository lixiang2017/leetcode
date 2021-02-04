'''
approach: Hash Table
Time: O(klogk + N + k), where k is the distinct number of nums and N is the total number of nums.
Space: O(k + k) = O(k)

You are here!
Your runtime beats 63.40 % of python submissions.
You are here!
Your memory usage beats 11.11 % of python submissions.
'''


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        harmonious = 0
        keys = sorted(list(set(nums)))
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        for i, j in zip([keys[0]] + keys ,keys):
            if i + 1 == j:
                harmonious = max(harmonious, count[i] + count[j])

        return harmonious
