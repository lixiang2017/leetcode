'''
approach: Hash Table + PrefixSum
Time: O(N)
Space: O(N)

执行用时：68 ms, 在所有 Python3 提交中击败了37.66%的用户
内存消耗：17.7 MB, 在所有 Python3 提交中击败了58.87%的用户
'''

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        height = len(wall)
        broken = defaultdict(int)
        max_broken = 0
        for row in wall:
            N = len(row)
            preSum = 0
            for i in range(N - 1):
                preSum += row[i]
                broken[preSum] += 1
                if broken[preSum] > max_broken:
                    max_broken = broken[preSum]

        return height - max_broken
