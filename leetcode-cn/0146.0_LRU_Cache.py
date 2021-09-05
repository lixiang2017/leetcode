'''
collections.OrderedDict

执行用时：484 ms, 在所有 Python3 提交中击败了86.72% 的用户
内存消耗：71.2 MB, 在所有 Python3 提交中击败了16.98% 的用户
通过测试用例：22 / 22
'''
class LRUCache(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
