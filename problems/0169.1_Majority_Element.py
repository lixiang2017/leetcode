

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1

        for num in nums:
            if hashmap[num] > len(nums) / 2:
                return num



if __name__ == '__main__':
    nums = [3,2,3]
    assert Solution().majorityElement(nums) == 3

    nums = [2,2,1,1,1,2,2]
    assert Solution().majorityElement(nums) == 2

    nums = [6,5,5]
    assert Solution().majorityElement(nums) == 5
