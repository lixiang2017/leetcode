'''
差分数组
Time: O(M + N)
Space: O(2N)

执行用时：100 ms, 在所有 Python3 提交中击败了91.67%的用户
内存消耗：24.4 MB, 在所有 Python3 提交中击败了62.05%的用户
通过测试用例：
63 / 63
'''
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 2)
        for first, last, seats in bookings:
            diff[first] += seats
            diff[last + 1] -= seats 
        presum = list(accumulate(diff))
        return presum[1:-1]
