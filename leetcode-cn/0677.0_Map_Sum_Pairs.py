'''
执行用时：20 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了49.06% 的用户
通过测试用例：35 / 35
'''
class MapSum:

    def __init__(self):
        self.seen = dict()
        self.m = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        if key in self.seen:
            old_val = self.seen[key]
            for i in range(1, len(key) + 1):
                self.m[key[: i]] += val - old_val
        else:
            for i in range(1, len(key) + 1):
                self.m[key[: i]] += val
        self.seen[key] = val

    def sum(self, prefix: str) -> int:
        return self.m[prefix]


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
