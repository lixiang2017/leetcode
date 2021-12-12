'''
Runtime: 428 ms, faster than 79.69% of Python3 online submissions for Partition Equal Subset Sum.
Memory Usage: 14.8 MB, less than 66.76% of Python3 online submissions for Partition Equal Subset Sum.
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        
        s = set([0])
        for x in nums:
            sum_with_x = set()
            for ss in s:
                if x + ss == target:
                    return True
                elif x + ss < target:
                    sum_with_x.add(x + ss)
            s.update(sum_with_x)
            
        return False
        