'''
T: O(N), S:O(1)

执行用时：68 ms, 在所有 Python3 提交中击败了63.64% 的用户
内存消耗：24 MB, 在所有 Python3 提交中击败了37.34% 的用户
通过测试用例：76 / 76
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = min2 = None
        for x in nums:
            if min1 is None:
                min1 = x
            else:
                if x < min1:
                    min1 = x
                elif x > min1:
                    if min2 is None:
                        min2 = x
                    else:
                        if x < min2:
                            min2 = x
                        elif x > min2:
                            return True
        return False


'''
T: O(N), S:O(1)

执行用时：64 ms, 在所有 Python3 提交中击败了73.43% 的用户
内存消耗：24.1 MB, 在所有 Python3 提交中击败了13.78% 的用户
通过测试用例：76 / 76
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = min2 = None
        for x in nums:
            if min1 is None:
                min1 = x
            elif x < min1:
                min1 = x
            elif x > min1:
                if min2 is None:
                    min2 = x
                elif x < min2:
                    min2 = x
                elif x > min2:
                    return True
        return False


'''
执行用时：56 ms, 在所有 Python3 提交中击败了92.10% 的用户
内存消耗：24 MB, 在所有 Python3 提交中击败了41.89% 的用户
通过测试用例：76 / 76
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small, mid = float('inf'), float('inf')
        for x in nums:
            if x <= small:
                small = x
            elif x <= mid:
                mid = x
            else:
                return True
        return False


'''
执行用时：116 ms, 在所有 Python3 提交中击败了17.20% 的用户
内存消耗：24 MB, 在所有 Python3 提交中击败了40.91% 的用户
通过测试用例：76 / 76
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        q = []
        for x in nums:
            idx = bisect_left(q, x)
            if idx == len(q):
                q.append(x)
            else:
                q[idx] = x
            if len(q) == 3:
                return True
        return False
