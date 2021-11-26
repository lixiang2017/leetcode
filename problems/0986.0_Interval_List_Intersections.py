'''
Two Pointers
T: O(M + N)
S: O(1)

Runtime: 140 ms, faster than 95.30% of Python3 online submissions for Interval List Intersections.
Memory Usage: 15.4 MB, less than 9.89% of Python3 online submissions for Interval List Intersections.
'''
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        m, n = len(firstList), len(secondList)
        i = j = 0
        while i < m and j < n:
            # first start, first end
            fs, fe = firstList[i]
            # second start, second end
            ss, se = secondList[j]
            if fe < ss:
                i += 1
                continue
            if se < fs:
                j += 1
                continue
            if fe <= se:
                ans.append([max(fs, ss), fe])
                i += 1
                continue
            if se <= fe:
                ans.append([max(fs, ss), se])
                j += 1
                continue

        return ans

'''
执行用时：56 ms, 在所有 Python3 提交中击败了20.25% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了47.13% 的用户
通过测试用例：85 / 85
'''
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        m, n = len(firstList), len(secondList)
        i = j = 0
        while i < m and j < n:
            # first start, first end
            fs, fe = firstList[i]
            # second start, second end
            ss, se = secondList[j]
            l, r = max(fs, ss), min(fe, se)
            if l <= r:
                ans += [[l, r]]
            if fe < se:
                i += 1
            else:
                j += 1

        return ans
        