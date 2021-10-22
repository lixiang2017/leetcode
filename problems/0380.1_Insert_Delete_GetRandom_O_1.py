'''
Runtime: 416 ms, faster than 92.08% of Python3 online submissions for Insert Delete GetRandom O(1).
Memory Usage: 61.7 MB, less than 67.41% of Python3 online submissions for Insert Delete GetRandom O(1).
'''
class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        idx = self.pos[val]
        last = self.nums[-1]
        self.nums[idx] = last
        self.pos[last] = idx
        self.nums.pop()
        self.pos.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
