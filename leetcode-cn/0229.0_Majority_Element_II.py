'''
摩尔投票法
T: O(2N)
S: O(1)

执行用时：48 ms, 在所有 Python3 提交中击败了26.45% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了5.13% 的用户
通过测试用例：82 / 82
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element1 = element2 = 0
        vote1 = vote2 = 0
        for x in nums:
            if vote1 > 0 and element1 == x:
                vote1 += 1
            elif vote2 > 0 and element2 == x:
                vote2 += 1
            elif vote1 == 0:
                element1 = x
                vote1 = 1
            elif vote2 == 0:
                element2 = x
                vote2 = 1
            else:
                vote1 -= 1
                vote2 -= 1
        
        cnt1 = cnt2 = 0
        for x in nums:
            if x == element1:
                cnt1 += 1
            elif x == element2:
                cnt2 += 1
        ans = []
        if cnt1 > len(nums) // 3:
            ans.append(element1)
        if cnt2 > len(nums) // 3:
            ans.append(element2)
        return ans
        
