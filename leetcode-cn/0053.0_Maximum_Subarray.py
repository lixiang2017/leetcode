'''
T: O(N)
S: O(1)

执行用时：100 ms, 在所有 Python3 提交中击败了76.84% 的用户
内存消耗：25.2 MB, 在所有 Python3 提交中击败了69.19% 的用户
通过测试用例：209 / 209
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        pre = 0
        for x in nums:
            if pre >= 0:
                pre += x
            else:
                pre = x
            ans = max(ans, pre)
        return ans


'''
执行用时：148 ms, 在所有 Python3 提交中击败了76.08% 的用户
内存消耗：25.5 MB, 在所有 Python3 提交中击败了93.95% 的用户
通过测试用例：209 / 209
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        pre = 0
        for x in nums:
            pre += x
            ans = max(ans, pre)
            if pre < 0:
                pre = 0

        return ans 


'''
segment tree
分治思想

执行用时：1064 ms, 在所有 Python3 提交中击败了5.03% 的用户
内存消耗：26.1 MB, 在所有 Python3 提交中击败了24.23% 的用户
通过测试用例：209 / 209
'''
class Status:
    def __init__(self, lSum, rSum, mSum, iSum):
        self.lSum = lSum 
        self.rSum = rSum 
        self.mSum = mSum 
        self.iSum = iSum 

def getInfo(nums, l, r) -> Status:
    if l == r:
        return Status(nums[l], nums[l], nums[l], nums[l])
    m = (l + r) >> 1
    lSub = getInfo(nums, l, m)
    rSub = getInfo(nums, m + 1, r)
    return pushUp(lSub, rSub)

def pushUp(l: Status, r: Status) -> Status:
    iSum = l.iSum + r.iSum 
    lSum = max(l.lSum, l.iSum + r.lSum)
    rSum = max(r.rSum, r.iSum + l.rSum)
    mSum = max(l.mSum, r.mSum, l.rSum + r.lSum)
    return Status(lSum, rSum, mSum, iSum)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return getInfo(nums, 0, len(nums) - 1).mSum 


'''
segment tree
分治思想

执行用时：1052 ms, 在所有 Python3 提交中击败了5.03% 的用户
内存消耗：25.7 MB, 在所有 Python3 提交中击败了58.52% 的用户
通过测试用例：209 / 209
'''
class Status:
    def __init__(self, lSum, rSum, mSum, iSum):
        self.lSum = lSum 
        self.rSum = rSum 
        self.mSum = mSum 
        self.iSum = iSum 

    @classmethod
    def getInfo(cls, nums: List[int], l: int, r: int):
        if l == r:
            return Status(nums[l], nums[l], nums[l], nums[l])
        m = (l + r) >> 1
        lSub = cls.getInfo(nums, l, m)
        rSub = cls.getInfo(nums, m + 1, r)
        return cls.pushUp(lSub, rSub)

    @classmethod
    def pushUp(cls, l, r):
        iSum = l.iSum + r.iSum 
        lSum = max(l.lSum, l.iSum + r.lSum)
        rSum = max(r.rSum, r.iSum + l.rSum)
        mSum = max(l.mSum, r.mSum, l.rSum + r.lSum)
        return Status(lSum, rSum, mSum, iSum)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return Status.getInfo(nums, 0, len(nums) - 1).mSum 


