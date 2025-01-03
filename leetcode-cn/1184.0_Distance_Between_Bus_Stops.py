'''
执行用时：36 ms, 在所有 Python3 提交中击败了68.51% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了65.26% 的用户
通过测试用例：37 / 37
'''
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s = sum(distance)
        if start > destination:
            start, destination = destination, start
        one = sum(distance[start: destination])
        return min(one, s - one)

'''
执行用时：40 ms, 在所有 Python3 提交中击败了40.33% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了41.67% 的用户
通过测试用例：37 / 37
'''
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s = sum(distance)
        if start > destination:
            start, destination = destination, start
        s1 = sum(distance[start: destination])
        return min(s1, s - s1)

