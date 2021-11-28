'''
Prefix Product + Post Product
T: O(3N)
S: O(2N)

Runtime: 356 ms, faster than 14.51% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 22.3 MB, less than 23.58% of Python3 online submissions for Product of Array Except Self.
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        pre, post = [1] * N, [1] * N
        for i, x in enumerate(nums):
            if i == 0:
                pre[0] = nums[i]
            else:
                pre[i] = pre[i - 1] * nums[i]
        for i in range(N - 1, -1, -1):
            if i == N - 1:
                post[i] = nums[i]
            else:
                post[i] = post[i + 1] * nums[i]
        
        ans = [1] * N
        for i in range(N):
            if i == 0:
                ans[i] = post[1]
            elif i == N - 1:
                ans[i] = pre[i - 1]
            else:
                ans[i] = pre[i - 1] * post[i + 1]
        return ans

'''
Prefix Product + Post Product
T: O(2N)
S: O(1)

ref:
https://leetcode.com/problems/product-of-array-except-self/discuss/65625/Python-solution-(Accepted)-O(n)-time-O(1)-space

Runtime: 456 ms, faster than 5.02% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 21 MB, less than 81.43% of Python3 online submissions for Product of Array Except Self.
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        n = len(nums)
        ans = []
        for i in range(n):
            ans.append(p)
            p *= nums[i]
            
        p = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= p
            p *= nums[i]
        
        return ans


'''
Prefix Product + Post Product
from beginnging to end
T: O(N)
S: O(1)

Runtime: 240 ms, faster than 68.66% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 21.2 MB, less than 47.25% of Python3 online submissions for Product of Array Except Self.
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        pre = post = 1
        for i in range(n):
            j = n - 1 - i  # j = - 1 - i
            ans[i] *= pre
            ans[j] *= post
            pre *= nums[i]
            post *= nums[j]
        return ans


'''
Prefix Product + Post Product
from end to beginning
T: O(N)
S: O(1)

Runtime: 302 ms, faster than 23.79% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 21.2 MB, less than 47.25% of Python3 online submissions for Product of Array Except Self.
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        pre = post = 1
        for j in range(n - 1, -1, -1):
            i = n - 1 - j   # i = - 1 - j
            ans[i] *= pre
            ans[j] *= post
            pre *= nums[i]
            post *= nums[j]
        return ans

'''
Prefix Product + Post Product
from beginnging to end
T: O(N)
S: O(1)

Runtime: 227 ms, faster than 92.62% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 21.2 MB, less than 58.80% of Python3 online submissions for Product of Array Except Self.
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in nums]
        left = right = 1
        for i, x in enumerate(nums):
            ans[i] *= left
            ans[- 1 - i] *= right
            left *= nums[i]
            right *= nums[- 1 - i]
        return ans

'''
Prefix Product + Post Product
from beginnging to end
T: O(N)
S: O(1)
You could equally use unitary tilde operator '~' too (which complements the number: 0 -> -1 , 1 -> -2, ... )

Runtime: 276 ms, faster than 29.99% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 21.3 MB, less than 47.25% of Python3 online submissions for Product of Array Except Self.
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        left = right = 1
        for i, x in enumerate(nums):
            ans[i] *= left
            ans[~i] *= right
            left *= nums[i]
            right *= nums[~i]
        return ans
