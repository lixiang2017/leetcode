'''
Runtime: 196 ms, faster than 99.29% of Python3 online submissions for Rotate Array.
Memory Usage: 25.6 MB, less than 12.78% of Python3 online submissions for Rotate Array.
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k: ] + nums[: -k]

'''
Runtime: 344 ms, faster than 38.01% of Python3 online submissions for Rotate Array.
Memory Usage: 25.4 MB, less than 96.40% of Python3 online submissions for Rotate Array.
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[n - k: ] + nums[: n - k]
                       
                       


'''
Runtime: 346 ms, faster than 30.06% of Python3 online submissions for Rotate Array.
Memory Usage: 25.5 MB, less than 83.73% of Python3 online submissions for Rotate Array.
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        # former, post. f1 f2 p1 p2
        f1, f2, p1, p2 = 0, n-k-1, n-k, n-1
        while f1 < f2:
            nums[f1], nums[f2] = nums[f2], nums[f1]
            f1 += 1
            f2 -= 1
        while p1 < p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 -= 1
        l, r = 0, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


'''
Runtime: 232 ms, faster than 56.27% of Python3 online submissions for Rotate Array.
Memory Usage: 25.6 MB, less than 54.66% of Python3 online submissions for Rotate Array.
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        
        l, r = 0, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1        
            
        # former, post. f1 f2 p1 p2
        # f1, f2, p1, p2 = 0, n-k-1, n-k, n-1
        f1, f2, p1, p2 = 0, k-1, k, n-1
        while f1 < f2:
            nums[f1], nums[f2] = nums[f2], nums[f1]
            f1 += 1
            f2 -= 1
        while p1 < p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 -= 1


'''
Runtime: 292 ms, faster than 38.37% of Python3 online submissions for Rotate Array.
Memory Usage: 25.7 MB, less than 12.78% of Python3 online submissions for Rotate Array.
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
        
    def reverse(self, arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1        



'''
Runtime: 494 ms, faster than 20.73% of Python3 online submissions for Rotate Array.
Memory Usage: 25.5 MB, less than 56.82% of Python3 online submissions for Rotate Array.
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)
        
    def reverse(self, arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1        
                       






