'''
13 小时，13 分钟 ago 	Find Unique Binary String 	Accepted
'''

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums)
        seen = set(int(num, 2) for num in nums)
        for i in range(1 << N):
            if i not in seen:
                return bin(i)[2:].zfill(N)
