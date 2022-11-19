'''
Time: O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：20 ms, 在所有 Python 提交中击败了63.86%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了21.69%的用户
'''

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        highest = current = 0
        for diff in gain:
            current += diff
            highest = max(highest, current)

        return highest


'''
执行用时：40 ms, 在所有 Python3 提交中击败了46.30% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了42.80% 的用户
通过测试用例：80 / 80
'''
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = altitude = 0
        for g in gain:
            altitude += g 
            highest = max(highest, altitude)
        return highest

'''
执行用时：40 ms, 在所有 Python3 提交中击败了46.30% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了89.49% 的用户
通过测试用例：80 / 80
'''
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(0, max(accumulate(gain)))


'''
执行用时：32 ms, 在所有 Python3 提交中击败了89.49% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了17.90% 的用户
通过测试用例：80 / 80
'''
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(accumulate(gain, initial=0))
