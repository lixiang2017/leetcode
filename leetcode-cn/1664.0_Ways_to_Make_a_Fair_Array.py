'''
simulation
T: O(2N) = O(N)
S: O(1)

执行用时：328 ms, 在所有 Python3 提交中击败了51.61% 的用户
内存消耗：19.2 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：105 / 105
'''
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        total_even = total_odd = 0
        for i, x in enumerate(nums):
            if i & 1:
                total_odd += x 
            else:
                total_even += x 
        ans = 0
        cur_even = cur_odd = 0
        for i, x in enumerate(nums):
            # try to remove x 
            if i & 1:
                right_odd = total_odd - x - cur_odd   # will become even
                right_even = total_even - cur_even    # will become odd
                if cur_even + right_odd == cur_odd + right_even:
                    ans += 1
            else:
                right_odd = total_odd - cur_odd           # will become even
                right_even = total_even - x - cur_even    # will become odd
                if cur_even + right_odd == cur_odd + right_even:
                    ans += 1                

            # post process, add x 
            if i & 1:
                cur_odd += x 
            else:
                cur_even += x 

        return ans 
