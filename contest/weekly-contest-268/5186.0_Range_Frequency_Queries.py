'''
20 / 20 个通过测试用例
状态：通过
执行用时: 832 ms
内存消耗: 52.7 MB
'''
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.freq = defaultdict(list)
        for i, a in enumerate(arr):
            self.freq[a].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if not self.freq[value]:
            return 0
        l = bisect_left(self.freq[value], left)
        r = bisect_right(self.freq[value], right)
        return r - l



# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)



'''
执行用时：708 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：52.7 MB, 在所有 Python3 提交中击败了50.00% 的用户
通过测试用例：20 / 20
'''
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.freq = defaultdict(list)
        for i, a in enumerate(arr):
            self.freq[a].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        return bisect_right(self.freq[value], right) - bisect_left(self.freq[value], left)

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)


