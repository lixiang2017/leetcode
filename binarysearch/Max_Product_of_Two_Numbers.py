'''
T: O(N)
S: O(1)

Success!
Your code took 148 milliseconds — faster than 9.43% in Python
'''

class Solution:
    def solve(self, nums):
        N = len(nums)
        if N < 2:
            return 0
        elif 2 == N:
            return nums[0] * nums[1]
        elif 3 == N:
            return max(nums[0] * nums[1], nums[0] * nums[2], nums[1] * nums[2])
        # high, low
        high1 = high2 = product = -0x3F3F3F3F
        low1 = low2 = 0
        for num in nums:
            if num >= high1:
                high2 = high1
                high1 = num
            elif num >= high2:
                high2 = num

            if num < 0 and abs(num) >= abs(low1):
                low2 = low1
                low1 = num
            elif num < 0 and abs(num) >=  abs(low2):
                low2 = num

        product = max(product, high1 * high2)
        if low1 < 0 and low2 < 0:
            product = max(product, low1 * low2)
        return product

'''
T: O(N)
S: O(1)

Your code took 468 milliseconds — faster than 0.65% in Python

ref:
https://binarysearch.com/problems/Max-Product-of-Two-Numbers/editorials/3764405
'''
class Solution:
    def solve(self, nums):
        ans, N = -0x3f3f3f, len(nums)
        minval = maxval = nums[0]
        for i in range(1, N):
            ans = max(ans, minval * nums[i], maxval * nums[i])
            minval = min(minval, nums[i])
            maxval = max(maxval, nums[i])
        return ans

'''
Wrong Answer
Testcase
nums = [2, -3]
Your result
0
Expected
-6
'''       

