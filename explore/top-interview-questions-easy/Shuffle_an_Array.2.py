'''
Fisher-Yates

You are here!
Your runtime beats 88.96 % of python submissions.
'''


import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = nums
        self.array = list(nums)
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.array)):
            swp_index = random.randrange(len(self.array))
            # swp_index =  random.randrange(i, len(self.array))    # also Accepted
            self.array[i], self.array[swp_index] = self.array[swp_index], self.array[i]
        return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()