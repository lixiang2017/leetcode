'''
brute force

执行用时：8616 ms, 在所有 Python3 提交中击败了12.88% 的用户
内存消耗：30.4 MB, 在所有 Python3 提交中击败了62.12% 的用户
通过测试用例：17 / 17
'''
class AllOne:

    def __init__(self):
        self.d = Counter()

    def inc(self, key: str) -> None:
        self.d[key] += 1

    def dec(self, key: str) -> None:
        self.d[key] -= 1
        if self.d[key] == 0:
            self.d.pop(key)

    def getMaxKey(self) -> str:
        key, cnt = '', 0
        for k, c in self.d.items():
            if c > cnt:
                cnt = c 
                key = k 
        return key

    def getMinKey(self) -> str:
        key, cnt = '', float('inf')
        for k, c in self.d.items():
            if c < cnt:
                cnt = c 
                key = k 
        return key 

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
