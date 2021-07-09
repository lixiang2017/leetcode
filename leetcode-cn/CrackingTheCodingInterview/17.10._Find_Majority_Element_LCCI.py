'''
Boyer-Moore,T:O(2N),S:O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了93.25% 的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了5.10% 的用户
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = -1
        cnt = 0
        for num in nums:
            if cnt == 0:
                candidate = num
                cnt = 1
            else:
                if num == candidate:
                    cnt += 1
                else:
                    cnt -= 1
                    
        N = len(nums)
        cnt = 0
        for num in nums:
            if num == candidate:
                cnt += 1
                if cnt > N // 2:
                    return candidate

        return -1
