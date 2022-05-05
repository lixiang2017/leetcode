'''
执行用时：36 ms, 在所有 Python3 提交中击败了95.74% 的用户
内存消耗：21 MB, 在所有 Python3 提交中击败了87.38% 的用户
通过测试用例：38 / 38
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n 
        nums[:] = nums[-k: ] + nums[: -k]

'''
reverse * 3

执行用时：52 ms, 在所有 Python3 提交中击败了48.21% 的用户
内存消耗：21.2 MB, 在所有 Python3 提交中击败了42.88% 的用户
通过测试用例：38 / 38
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n 
        # 0     n-k-1 | n-k      n-1
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)
    
    def reverse(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
