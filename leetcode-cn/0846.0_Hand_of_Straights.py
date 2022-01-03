'''
heapq

执行用时：124 ms, 在所有 Python3 提交中击败了56.74% 的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了9.55% 的用户
通过测试用例：73 / 73
'''
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = Counter(hand)
        h = list(c.keys())
        heapify(h)
        while h:
            start = heappop(h)
            while h and start not in c:
                if not h:
                    return False 
                start = heappop(h)
            if start not in c:
                break

            for i in range(1, groupSize):
                if start + i not in c or c[start] > c[start + i]:
                    return False
                c[start + i] -= c[start]
                if c[start + i] == 0:
                    del c[start + i]
            del c[start]

        return True

'''
Counter + sort

执行用时：64 ms, 在所有 Python3 提交中击败了93.82% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了46.63% 的用户
通过测试用例：73 / 73
'''
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = Counter(hand)
        for x in sorted(c.keys()):
            if c[x] == 0:
                continue
            for j in range(1, groupSize):
                if x + j not in c or c[x] > c[x + j]:
                    return False
                c[x + j] -= c[x]
        return True

'''
执行用时：72 ms, 在所有 Python3 提交中击败了85.39% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了62.36% 的用户
通过测试用例：73 / 73
'''
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        c = Counter(hand)
        for x in sorted(c.keys()):
            if c[x] == 0:
                continue
            for j in range(1, groupSize):
                if x + j not in c or c[x] > c[x + j]:
                    return False
                c[x + j] -= c[x]
        return True


