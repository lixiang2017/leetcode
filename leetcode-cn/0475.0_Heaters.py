'''
sort + two pointers

执行用时：96 ms, 在所有 Python3 提交中击败了70.40% 的用户
内存消耗：17.5 MB, 在所有 Python3 提交中击败了61.58% 的用户
通过测试用例：30 / 30
'''
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        ans = 0
        j, n = 0, len(heaters)
        for house in houses:
            r = float('inf')
            while j < n and heaters[j] < house:
                j += 1
            if j - 1 >= 0:
                r = min(r, abs(heaters[j - 1] - house))
            if j < n:
                r = min(r, abs(heaters[j] - house))
            ans = max(ans, r)
        return ans 
