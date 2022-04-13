'''
dict + list

执行用时：464 ms, 在所有 Python3 提交中击败了45.15% 的用户
内存消耗：49.7 MB, 在所有 Python3 提交中击败了55.92% 的用户
通过测试用例：19 / 19
'''
class RandomizedSet:

    def __init__(self):
        # val -> idx in list
        self.d = dict()
        # just append/pop val to/from list
        self.l = list()

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        else:
            self.l.append(val)
            self.d[val] = len(self.l) - 1
            return True    

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        else:
            to_delete_idx = self.d[val]
            last_one = self.l[-1]
            self.l[to_delete_idx] = last_one
            self.d[last_one] = to_delete_idx
            self.d.pop(val)
            self.l.pop()
            return True 

    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
