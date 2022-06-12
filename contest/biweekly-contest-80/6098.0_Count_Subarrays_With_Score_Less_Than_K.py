'''
sliding window, 每次以 i 为起始下标，寻找满足条件的（最大可能的） 以 j - 1 为结束下标

执行用时：364 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：26.3 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：167 / 167
'''
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        ans = 0
        i = j = 0
        for i in range(n):
            while j < n and (nums[j] - (nums[i - 1] if i else 0)) * (j - i + 1) < k:
                j += 1
            ans += j - i
        return ans 


'''
while i < n

不能使用 while i < n and j < n  ！！！ 因为后面可能很多次都要使用 j == n, ans += n - i

执行用时：368 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：26.4 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：167 / 167
'''
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        ans = 0
        i = j = 0
        while i < n:
            while j < n and (nums[j] - (nums[i - 1] if i else 0)) * (j - i + 1) < k:
                j += 1
            ans += j - i
            # move to next i
            i += 1
        return ans 

'''
sliding window, 每次以 j 为结束下标, 寻找满足条件的 i 为起始下标

执行用时：352 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：26.4 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：167 / 167
'''
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        ans = 0
        i = 0
        for j in range(n):
            while i <= j and (nums[j] - (nums[i - 1] if i else 0)) * (j - i + 1) >= k:
                i += 1
            ans += j - i + 1
        return ans 

'''
while j < n:

执行用时：372 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：26.1 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：167 / 167
'''
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        ans = 0
        i = j = 0
        while j < n:
            while i <= j and (nums[j] - (nums[i - 1] if i else 0)) * (j - i + 1) >= k:
                i += 1
            ans += j - i + 1
            # move to next j 
            j += 1
        return ans 

'''
执行用时：200 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：25 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：167 / 167
'''
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans, subsum, length = 0, 0, 0
        for i, num in enumerate(nums):
            length += 1
            subsum += num 
            while length * subsum >= k:
                subsum -= nums[i - length + 1]
                length -= 1
            ans += length
        return ans 


        
