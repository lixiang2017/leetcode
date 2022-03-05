'''
DP

Runtime: 64 ms, faster than 77.59% of Python3 online submissions for Delete and Earn.
Memory Usage: 14.3 MB, less than 54.80% of Python3 online submissions for Delete and Earn.
'''
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = Counter(nums)
        distinct = sorted(set(nums))
        n = len(distinct)
        earn = [[0, 0] for _ in range(n + 1)]
        for i in range(n):
            # 0, delete;  1, not delete
            earn[i + 1][0] = earn[i][1] + distinct[i] * c[distinct[i]]
            if i > 0 and distinct[i - 1] + 1 != distinct[i]:
                earn[i + 1][0] = max(earn[i + 1][0], earn[i][0] + distinct[i] * c[distinct[i]])
                                                          
            earn[i + 1][1] = max(earn[i][0], earn[i][1])
        
        return max(earn[-1][0], earn[-1][1])
        
        
