'''
heap

执行用时：264 ms, 在所有 Python3 提交中击败了72.31% 的用户
内存消耗：19 MB, 在所有 Python3 提交中击败了72.31% 的用户
通过测试用例：69 / 69
'''
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        ans, latest = 0, -1
        n = len(apples)
        h = []
        for i in range(n):
            while h and h[0][0] <= i:
                heappop(h)

            if apples[i]:
                heappush(h, (i + days[i], apples[i]))

            if h:
                d, a = heappop(h)
                a -= 1
                ans += 1
                if a > 0:
                    heappush(h, (d, a))

        latest = n
        while h:
            while h and h[0][0] <= latest:
                heappop(h)
            if not h:
                break
            d, a = heappop(h)
            ans += min(d - latest, a)
            latest += min(d - latest, a)

        return ans

'''
执行用时：228 ms, 在所有 Python3 提交中击败了76.92% 的用户
内存消耗：19.3 MB, 在所有 Python3 提交中击败了20.00% 的用户
通过测试用例：69 / 69
'''
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        ans, latest = 0, -1
        n = len(apples)
        h = []
        for i in range(n):
            while h and h[0][0] <= i:
                heappop(h)

            if apples[i]:
                heappush(h, [i + days[i], apples[i]])

            if h:
                h[0][1] -= 1
                ans += 1
                if h[0][1] == 0:
                    heappop(h)

        latest = n
        while h:
            while h and h[0][0] <= latest:
                heappop(h)
            if not h:
                break
            d, a = heappop(h)
            ans += min(d - latest, a)
            latest += min(d - latest, a)

        return ans
        