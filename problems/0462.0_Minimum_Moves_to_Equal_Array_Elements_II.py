'''
Runtime: 157 ms, faster than 12.32% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
Memory Usage: 15.4 MB, less than 79.18% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
'''
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        return sum(abs(x - nums[len(nums) // 2]) for x in nums)

'''
quick select
T: O(N + N/2 + N/4 + N/8 + N/16 + ...) = O(2N) = O(N)
S： O（logN）， for recursion stack

Runtime: 114 ms, faster than 50.28% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
Memory Usage: 15.6 MB, less than 5.10% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
'''
class Helper:
    
    @staticmethod
    def partition(nums: List[int], l: int, r: int) -> int:
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1
        
    @staticmethod
    def randomPartition(nums: List[int], l: int, r: int) -> int:
        idx = randint(l, r)
        nums[idx], nums[r] = nums[r], nums[idx]
        return Helper.partition(nums, l, r)
    
    @staticmethod
    def quickSelected(nums: List[int], l: int, r: int, k: int) -> int:
        index = Helper.randomPartition(nums, l, r)
        if index == k:
            return nums[index]
        elif index < k:
            return Helper.quickSelected(nums, index + 1, r, k)
        else:
            return Helper.quickSelected(nums, l, index - 1, k)

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        seed(time())
        mid_value = Helper.quickSelected(nums, 0, len(nums) - 1, len(nums) // 2)
        return sum(abs(x - mid_value) for x in nums)
    

