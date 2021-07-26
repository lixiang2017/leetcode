'''
You are here!
Your runtime beats 96.24 % of python3 submissions
You are here!
Your memory usage beats 38.73 % of python3 submissions.
'''
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.origin = nums[:]
        self.nums = nums
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.origin

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.nums)
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()



'''
You are here!
Your runtime beats 98.88 % of python3 submissions.
You are here!
Your memory usage beats 98.22 % of python3 submissions.
'''
class Solution:

    def __init__(self, nums: List[int]):
        self.origin = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.origin

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        return sorted(self.origin, key=lambda x: random.random())


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

