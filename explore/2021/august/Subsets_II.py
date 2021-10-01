'''
You are here!
Your runtime beats 51.18 % of python3 submissions.
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[]]
        for n in nums:
            before = copy.deepcopy(ans)
            for one in before:
                one.append(n)
                ans.append(one)
        ans = set([tuple(l) for l in ans])
        return ans

'''
You are here!
Your runtime beats 77.71 % of python3 submissions.
You are here!
Your memory usage beats 27.58 % of python3 submissions.
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[]]
        cur = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                cur = [item + [nums[i]] for item in cur]
            else:
                cur = [item + [nums[i]] for item in ans]
            ans += cur
        return ans