'''
Binary Search

执行用时：56 ms, 在所有 Python3 提交中击败了99.11% 的用户
内存消耗：19.1 MB, 在所有 Python3 提交中击败了83.93% 的用户
通过测试用例：9 / 9
'''
class SummaryRanges:

    def __init__(self):
        self._buffer = []

    def addNum(self, val: int) -> None:
        if not self._buffer:
            self._buffer.append([val, val])
        else:
            i = bisect.bisect_right(self._buffer, [val, val])
            # to link i-1_th
            t = []
            if i > 0:
                t.append(self._buffer[i - 1][:])
                if val <= t[-1][1] + 1:
                    t[-1][1] = max(val, t[-1][1])
                else:
                    t.append([val, val])
            else:
                t.append([val, val])
            # to link i_th
            if i < len(self._buffer):
                if t[-1][1] + 1 >= self._buffer[i][0]:
                    t[-1][1] = self._buffer[i][1]
                else:
                    t.append(self._buffer[i])
            self._buffer[max(0, i - 1): i + 1] = t

    def getIntervals(self) -> List[List[int]]:
        return self._buffer

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
