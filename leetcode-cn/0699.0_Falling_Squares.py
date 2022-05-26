'''
离散化+二分+暴力
T: O(N + 2N*log(2N) + N * (log2N + log2N + 2N)) = O(N^2)
S: O(2N + log2N + 2N + 2N + 2N) = O(N)

执行用时：84 ms, 在所有 Python3 提交中击败了92.17% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了86.96% 的用户
通过测试用例：44 / 44
'''
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        xs = set()
        for left, sl in positions:
            xs.add(left)
            xs.add(left + sl - 1)
        sorted_xs = sorted(xs)
        n = len(xs)
        # height
        h = [0] * n 
        max_h = 0
        ans = []
        for left, sl in positions:
            idx1 = bisect_left(sorted_xs, left)
            idx2 = bisect_left(sorted_xs, left + sl - 1)
            pre_h = max(h[idx1: idx2 + 1])
            h[idx1: idx2 + 1] = [pre_h + sl] * (idx2 - idx1 + 1) 
            max_h = max(max_h, pre_h + sl)
            ans.append(max_h)
        return ans

'''
离散化 + hash table + 暴力
T: O(N^2)
S: O(N)

执行用时：76 ms, 在所有 Python3 提交中击败了92.17% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了74.78% 的用户
通过测试用例：44 / 44
'''
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        xs = set()
        for left, sl in positions:
            xs.add(left)
            xs.add(left + sl - 1)
        sorted_xs = sorted(xs)
        x2idx = {x: idx for idx, x in enumerate(sorted_xs)}
        n = len(xs)
        # height
        h = [0] * n 
        max_h = 0
        ans = []
        for left, sl in positions:
            # idx1 = bisect_left(sorted_xs, left)
            # idx2 = bisect_left(sorted_xs, left + sl - 1)
            idx1, idx2 = x2idx[left], x2idx[left + sl - 1]
            pre_h = max(h[idx1: idx2 + 1])
            h[idx1: idx2 + 1] = [pre_h + sl] * (idx2 - idx1 + 1) 
            max_h = max(max_h, pre_h + sl)
            ans.append(max_h)
        return ans


'''
不用离散化，直接存整个结构。就是速度有点慢。猜测是因为离散化后去重了很多位置。
T: O(N^2)
S: O(N)

执行用时：884 ms, 在所有 Python3 提交中击败了11.30% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了81.74% 的用户
通过测试用例：44 / 44
'''
class Section:
    def __init__(self, left, right, height):
        self._left = left
        self._right = right 
        self._height = height 
    
    def isOverlap(self, start, end):
        return (start >= self._left and start <= self._right) or \
            (end >= self._left and end <= self._right) or \
            (start < self._left and end > self._right)

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        sections, ans, max_h = [], [], 0
        for left, sl in positions:
            start, end = left, left + sl - 1
            height = sl 
            for section in sections:
                if section.isOverlap(start, end):
                    height = max(height, section._height + sl)
            sections.append(Section(start, end, height))
            max_h = max(max_h, height)
            ans.append(max_h)
        return ans 


