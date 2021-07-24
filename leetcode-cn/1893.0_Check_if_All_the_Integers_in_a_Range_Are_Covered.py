'''
Hash Set
执行用时：28 ms, 在所有 Python3 提交中击败了98.20% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了79.35% 的用户
'''
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        cover = set()
        for r in ranges:
            for num in range(r[0], r[1] + 1):
                cover.add(num)
        for n in range(left, right + 1):
            if n not in cover:
                return False
        return True


'''
Sort+DP,TO(NlogN+N),S:O(1)
执行用时：44 ms, 在所有 Python3 提交中击败了40.39% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了38.97% 的用户
'''
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        for r in ranges:
            if left > right:
                return True
            if left < r[0]:
                return False
            elif r[0] <= left <= r[1]:
                left = r[1] + 1
        
        return left > right



'''
差分数组 + Prefix Sum / Line Sweep
Time: O(N + L)
Space: O(L)

执行用时：36 ms, 在所有 Python3 提交中击败了80.96% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了32.74% 的用户
'''
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52
        for r in ranges:
            diff[r[0]] += 1
            diff[r[1] + 1] -= 1

        # prefix sum
        curr = 0
        for i in range(51):
            curr += diff[i]
            if left <= i <= right and curr <= 0:
                return False
        return True
