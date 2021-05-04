'''
approach: Binary Search
Time: O(NlogN)
Space: O(1)

执行用时：360 ms, 在所有 Python3 提交中击败了47.13%的用户
内存消耗：17.3 MB, 在所有 Python3 提交中击败了5.33%的用户
'''

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (low + high) // 2
            days = 0
            pre_weight = 0
            for weight in weights:
                if pre_weight + weight > mid:
                    days += 1
                    pre_weight = weight
                else:
                    pre_weight += weight

            if (pre_weight == 0 and days > D) or \
                    (pre_weight != 0 and days + 1 > D) :
                low = mid + 1
            else:
                high = mid

        return low

