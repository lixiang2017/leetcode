'''
simulation

执行用时：68 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：19.6 MB, 在所有 Python3 提交中击败了98.26% 的用户
通过测试用例：58 / 58
'''
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        even = sum(x if x % 2 == 0 else 0 for x in nums)
        for val, index in queries:
            if nums[index] % 2 == 0:
                if val % 2 == 0:
                    even += val
                else:
                    even -= nums[index]
            else:
                if val % 2 == 0:
                    pass
                else:
                    even += nums[index] + val 
            nums[index] += val
            ans.append(even)
        return ans 

