'''
sort,T:O(NlogN),S:O(N)
执行用时：52 ms, 在所有 Python3 提交中击败了88.82% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了58.77% 的用户
'''
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n2 = sorted(nums)
        l, r = 0, len(n2) - 1
        while l <= r and nums[l] == n2[l]:
            l += 1
        while l <= r and nums[r] == n2[r]:
            r -= 1
        return r - l + 1




'''
two pass, Two Pointers,T:O(2N),S:O(1)

执行用时：48 ms, 在所有 Python3 提交中击败了93.12% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了51.86% 的用户
'''
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # -1, -1 !!!
        l, r, minn, maxn = -1, -1, float('inf'), float('-inf')
        # from left to right, to find r
        for i in range(len(nums)):
            if maxn > nums[i]:
                r = i
            else:
                maxn = nums[i]

        # from right to left, to find l
        for i in range(len(nums) - 1, -1, -1):
            if minn < nums[i]:
                l = i
            else:   
                minn = nums[i]

        return r - l + 1 if r != -1 else 0


'''
输入：
[1,2,3,3,3]
输出：
3
预期结果：
0
'''
