'''
brute force

执行用时：96 ms, 在所有 Python3 提交中击败了35.44% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了87.34% 的用户
通过测试用例：102 / 102
'''
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n, m = len(nums), len(l)
        ans = [False] * m

        def check(left, right):
            arr = sorted(nums[left: right + 1])
            d = arr[1] - arr[0]
            for a, b in pairwise(arr):
                if b - a != d:
                    return False
            return True

        for i, (left, right) in enumerate(zip(l, r)):
            if right > left:
                ans[i] = check(left, right)
        return ans 
