'''
https://www.bilibili.com/video/BV17W4y1S7WR

根据这道题的原理，有个有趣的小问题。假设有100个囚犯对应1~100的编号，现在在一个房间里放100个编号1~100的箱子，将1~100编号的100张纸条随机放入箱子当中（每个箱子一张）。

现在对每个囚犯，要求他们依次进入房间，每个人都有50次随机开箱机会，每次开箱之后必须原封不动地还原，如果在50次以内开到了内部放着自己编号的纸条的箱子，则提前离开房间。如果100个囚犯都找到了自己对应编号的纸条，则全部释放，否则全部继续关押。如果囚犯可以事先商量开箱策略，可以用什么样的策略提高他们的释放率。



simulation
T: O(N)
S: O(N)

执行用时：172 ms, 在所有 Python3 提交中击败了77.29% 的用户
内存消耗：25.7 MB, 在所有 Python3 提交中击败了67.68% 的用户
通过测试用例：885 / 885
'''
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        seen = [False] * n
        ans = group = 0 
        for i, x in enumerate(nums):
            if seen[x]:
                continue
            group = 0
            while not seen[x]:
                seen[x] = True 
                x = nums[x]
                group += 1
            ans = max(ans, group)
        return ans 

'''
in place
T: O(N)
S: O(1)

执行用时：136 ms, 在所有 Python3 提交中击败了96.94% 的用户
内存消耗：22.7 MB, 在所有 Python3 提交中击败了91.70% 的用户
通过测试用例：885 / 885
'''
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        ans = group = 0 
        for i, x in enumerate(nums):
            if x == -1:
                continue
            group = 0
            while not nums[i] == -1:
                old_idx = i 
                i = nums[i]
                nums[old_idx] = -1
                group += 1
            ans = max(ans, group)
        return ans 

