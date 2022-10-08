'''
sort
T: O(2NlogN + 2N) = O（NlogN）
S: O(2N) = O（N）

执行用时：240 ms, 在所有 Python3 提交中击败了50.25% 的用户
内存消耗：36.5 MB, 在所有 Python3 提交中击败了78.89% 的用户
通过测试用例：67 / 67
'''
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        ans = [-1] * n
        pairs2 = [(x, i) for i, x in enumerate(nums2)]
        pairs2.sort()
        nums1.sort()
        not_used = []
        i = 0
        for x, idx in pairs2:
            while i < n and nums1[i] <= x:
                not_used.append(nums1[i])
                i += 1
            if i == n:
                break 
            ans[idx] = nums1[i]
            i += 1
        # not used 
        for i, x in enumerate(ans):
            if x == -1:
                ans[i] = not_used.pop()
        return ans 

