'''
sliding window + BST(Binary Search Tree) / bucket

You are here!
Your runtime beats 15.99 % of python submissions.

'''

from sortedcontainers import SortedList

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        SList = SortedList()
        for i in range(len(nums)):
            if i > k:   SList.remove(nums[i - k - 1])
            pos1 = SortedList.bisect_left(SList, nums[i] - t)
            pos2 = SortedList.bisect_right(SList, nums[i] + t)

            if pos1 != pos2 and pos1 != len(SList): return True
            SList.add(nums[i])

        return False



if __name__ == '__main__':
    nums, k, t = [1,2,2,3,1], 3, 0
    assert Solution().containsNearbyAlmostDuplicate(nums, k, t)

    nums, k, t = [1,5,9,1,5,9], 2, 3
    assert not Solution().containsNearbyAlmostDuplicate(nums, k, t)

    nums, k, t = [1,0,1,1], 1, 2
    assert Solution().containsNearbyAlmostDuplicate(nums, k, t)    

