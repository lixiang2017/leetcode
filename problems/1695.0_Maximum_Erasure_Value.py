'''
sliding window / two pointers
滑动窗口的关键，假想固定一侧的指针。此方法是假想固定右侧指针
T: O(N)
S: O(N), for hash table

nums[j...i]

Runtime: 2723 ms, faster than 12.92% of Python3 online submissions for Maximum Erasure Value.
Memory Usage: 27.4 MB, less than 68.93% of Python3 online submissions for Maximum Erasure Value.
'''
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans, n, subsum, memo = 0, len(nums), 0, defaultdict(int)
        j = 0
        for i in range(n):
            while j < i and memo[nums[i]] > 0:
                memo[nums[j]] -= 1
                subsum -= nums[j]
                j += 1
            # update
            subsum += nums[i]
            memo[nums[i]] = 1
            ans = max(ans, subsum)
        return ans 

'''
while i < n
nums[j...i]

Runtime: 1894 ms, faster than 44.64% of Python3 online submissions for Maximum Erasure Value.
Memory Usage: 28.3 MB, less than 22.54% of Python3 online submissions for Maximum Erasure Value.
'''
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans, n, subsum, memo = 0, len(nums), 0, defaultdict(int)
        i = j = 0
        while i < n:
            while j < n and memo[nums[j]] == 0:
                memo[nums[j]] = 1
                subsum += nums[j]
                j += 1
            # update
            ans = max(ans, subsum)
            subsum -= nums[i]
            memo[nums[i]] -= 1
            # move to next i 
            i += 1
        return ans 
                    
        
'''
此方法是假想固定左侧指针
sliding window / two pointers

T: O(N)
S: O(N), for hash table

nums[i...j]

Runtime: 2535 ms, faster than 16.42% of Python3 online submissions for Maximum Erasure Value.
Memory Usage: 28.3 MB, less than 10.72% of Python3 online submissions for Maximum Erasure Value.
'''
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans, n, subsum, memo = 0, len(nums), 0, defaultdict(int)
        j = 0
        for i in range(n):
            while j < n and memo[nums[j]] == 0:
                memo[nums[j]] = 1
                subsum += nums[j]
                j += 1
            # update
            ans = max(ans, subsum)
            subsum -= nums[i]
            memo[nums[i]] -= 1
            
        return ans 
    

'''
nums[i...j]

Runtime: 2299 ms, faster than 22.98% of Python3 online submissions for Maximum Erasure Value.
Memory Usage: 28.4 MB, less than 10.72% of Python3 online submissions for Maximum Erasure Value.
'''
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans, n, subsum, memo = 0, len(nums), 0, defaultdict(int)
        i = j = 0
        while i < n:
            while j < n and memo[nums[j]] == 0:
                memo[nums[j]] = 1
                subsum += nums[j]
                j += 1
            # update
            ans = max(ans, subsum)
            subsum -= nums[i]
            memo[nums[i]] -= 1
            # move to next i 
            i += 1
        return ans 
    
            
        
'''
这里可以使用  while i < n and j < n，
因为不用计数了。而且再次缩小窗口也不影响答案。

Runtime: 2281 ms, faster than 23.42% of Python3 online submissions for Maximum Erasure Value.
Memory Usage: 28 MB, less than 38.51% of Python3 online submissions for Maximum Erasure Value.
'''
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans, n, subsum, memo = 0, len(nums), 0, defaultdict(int)
        i = j = 0
        while i < n and j < n:
            while j < n and memo[nums[j]] == 0:
                memo[nums[j]] = 1
                subsum += nums[j]
                j += 1
            # update
            ans = max(ans, subsum)
            subsum -= nums[i]
            memo[nums[i]] -= 1
            # move to next i 
            i += 1
        return ans 
    
            
        



