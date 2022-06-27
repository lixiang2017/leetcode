'''
就是找最大的数字

Runtime: 267 ms, faster than 32.38% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
Memory Usage: 14.8 MB, less than 30.52% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
'''
class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(reduce(max, n)), 1) 
