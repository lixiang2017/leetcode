'''
执行用时：56 ms, 在所有 Python3 提交中击败了97.22%的用户
内存消耗：20.3 MB, 在所有 Python3 提交中击败了34.16%的用户
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)


'''
执行用时：44 ms, 在所有 Python3 提交中击败了99.73% 的用户
内存消耗：21.2 MB, 在所有 Python3 提交中击败了33.74% 的用户
通过测试用例：13 / 13
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums 

'''
执行用时：408 ms, 在所有 Python3 提交中击败了58.87% 的用户
内存消耗：20.6 MB, 在所有 Python3 提交中击败了89.92% 的用户
通过测试用例：13 / 13
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums 
    
    def randomized_quicksort(self, nums: List[int], left: int, right: int) -> None:
        if left >= right:
            return 
        mid = self.randomized_partition(nums, left, right)
        self.randomized_quicksort(nums, left, mid - 1)
        self.randomized_quicksort(nums, mid + 1, right)

    def randomized_partition(self, nums: List[int], l: int, r: int) -> int:
        pivot = random.randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l - 1
        for j in range(l, r):
            if nums[j] < nums[r]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i 


