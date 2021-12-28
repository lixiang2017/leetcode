'''
sort + binary search
T: O(NlogN + 2NlogN)

执行用时：212 ms, 在所有 Python3 提交中击败了28.18% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了99.09% 的用户
通过测试用例：88 / 88
'''
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        ans = 0
        for i, age in enumerate(ages):
            low = 0.5 * age + 7
            idx1 = bisect_right(ages, low)
            idx2 = bisect_right(ages, age)
            if idx2 > idx1:
                ans += idx2 - idx1 - 1 

        return ans 


'''
sort + two pointers
T: O(NlogN + 2N)

执行用时：148 ms, 在所有 Python3 提交中击败了55.45% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了16.36% 的用户
通过测试用例：88 / 88
'''
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        ans = idx1 = idx2 = 0
        n = len(ages)
        for i, age in enumerate(ages):
            low = 0.5 * age + 7
            while idx1 < n and ages[idx1] <= low:
                idx1 += 1
            while idx2 < n and ages[idx2] == age:
                idx2 += 1
            if idx2 > idx1 + 1:
                ans += idx2 - idx1 - 1 

        return ans 


