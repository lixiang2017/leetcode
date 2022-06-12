'''
prefix sum + binary search
T: O(7 * N + NlogN) = O(NlogN)
S: O(2N)

Runtime: 2397 ms, faster than 8.98% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
Memory Usage: 28.4 MB, less than 44.81% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
'''
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        left = list(accumulate(nums))
        if left[-1] < x or (nums[0] > x and nums[-1] > x):
            return -1
        if nums[0] == x or nums[-1] == x:
            return 1
        
        right = list(reversed(list(accumulate(reversed(nums)))))
        ans = n + 1
        
        for i in range(1, n):
            if right[i] == x:
                ans = min(ans, n - i)
            elif left[i] == x:
                ans = min(ans, i + 1)
            else:
                idx = bisect_left(left, x - right[i], 0, i - 1)
                if left[idx] + right[i] == x:
                    # for right, i...n-1
                    ans = min(ans, idx + 1 + n - i)
        
        return -1 if ans == n + 1 else ans 



'''
nums.reverse()

Runtime: 1515 ms, faster than 60.15% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
Memory Usage: 28.1 MB, less than 50.24% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
'''
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        left = list(accumulate(nums))
        if left[-1] < x or (nums[0] > x and nums[-1] > x):
            return -1
        if nums[0] == x or nums[-1] == x:
            return 1
        
        nums.reverse()
        right = list(accumulate(nums))
        right.reverse()
        ans = n + 1
        
        for i in range(1, n):
            if right[i] == x:
                ans = min(ans, n - i)
            elif left[i] == x:
                ans = min(ans, i + 1)
            else:
                idx = bisect_left(left, x - right[i], 0, i - 1)
                if left[idx] + right[i] == x:
                    # for right, i...n-1
                    ans = min(ans, idx + 1 + n - i)
        
        return -1 if ans == n + 1 else ans 


'''
right[i] = right[i + 1] + nums[i]

Runtime: 2933 ms, faster than 5.20% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
Memory Usage: 28.2 MB, less than 50.24% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
'''
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        left = list(accumulate(nums))
        if left[-1] < x or (nums[0] > x and nums[-1] > x):
            return -1
        if nums[0] == x or nums[-1] == x:
            return 1
        
        right = [nums[-1]] * n
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] + nums[i]
        ans = n + 1
        
        for i in range(1, n):
            if right[i] == x:
                ans = min(ans, n - i)
            elif left[i] == x:
                ans = min(ans, i + 1)
            else:
                idx = bisect_left(left, x - right[i], 0, i - 1)
                if left[idx] + right[i] == x:
                    # for right, i...n-1
                    ans = min(ans, idx + 1 + n - i)
        
        return -1 if ans == n + 1 else ans 


'''
sliding window / two pointers
T: O(N)
S: O(1)

Runtime: 1683 ms, faster than 46.23% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
Memory Usage: 27.9 MB, less than 96.23% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
'''
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # to find complementary
        n, s = len(nums), sum(nums)
        if s < x or (nums[0] > x and nums[-1] > x):
            return -1
        if s == x:
            return n
        com = s - x
        i = j = 0
        subsum = 0
        longest_sub = 0
        while i < n and j <= n:
            if subsum < com:
                if j == n:
                    break
                subsum += nums[j]
                if subsum == com:
                    longest_sub = max(longest_sub, j - i + 1)   # [i...j]
                j += 1
            else:
                subsum -= nums[i]
                i += 1
                if subsum == com:
                    longest_sub = max(longest_sub, j - i)   # [i...j-1], caused by `j += 1`
                    
        return -1 if longest_sub == 0 else n - longest_sub
    
'''
Input: [8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309]
134365
Output: -1
Expected: 16

Input
[5,1,4,2,3]
6
Output
-1
Expected
2
'''


'''
sliding window / two pointers
T: O(N)
S: O(1)

Runtime: 1460 ms, faster than 64.63% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
Memory Usage: 28 MB, less than 62.03% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
'''
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # to find complementary
        n, s = len(nums), sum(nums)
        if s < x or (nums[0] > x and nums[-1] > x):
            return -1
        if s == x:
            return n
        com = s - x
        i = j = 0
        subsum = 0
        longest_sub = 0
        while i < n and j <= n:
            if subsum < com:
                if j == n:
                    break
                subsum += nums[j]
                j += 1
            elif subsum > com:
                subsum -= nums[i]
                i += 1
            else:
                longest_sub = max(longest_sub, j - i)   # [i...j-1]
                subsum -= nums[i]
                if j == n:
                    break
                subsum += nums[j]
                i += 1
                j += 1
                    
        return -1 if longest_sub == 0 else n - longest_sub
    



'''
hash table
T: O(2N) = O(N)
S: O(N)

Runtime: 2198 ms, faster than 13.69% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
Memory Usage: 35.8 MB, less than 29.25% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
'''
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # postsum -> idx
        post, postsum = {}, 0
        n = len(nums)
        post[0] = n
        for i in range(n - 1, -1, -1):
            postsum += nums[i]
            post[postsum] = i 
        presum = 0
        ans = n + 1
        if x in post:
            ans = n - post[x]
        for i in range(n):
            presum += nums[i]
            if x - presum in post and post[x - presum] > i:
                idx = post[x - presum]
                ans = min(ans, i + 1 + n - idx)
                
        return -1 if ans == n + 1 else ans 








