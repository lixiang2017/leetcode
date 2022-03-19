'''
group of stacks

执行用时：304 ms, 在所有 Python3 提交中击败了20.70% 的用户
内存消耗：23 MB, 在所有 Python3 提交中击败了15.23% 的用户
通过测试用例：37 / 37
'''
class FreqStack:

    def __init__(self):
        # val -> cnt
        self.freq = Counter()
        # 1 -> stack 
        # 2 -> stack 
        # 3 -> stack
        #  ... 
        # max_freq -> stack
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        # T: O(1)
        self.freq[val] += 1
        f = self.freq[val]
        self.group[f].append(val)
        self.max_freq = max(self.max_freq, f)

    def pop(self) -> int:
        # T: O(1)
        x = self.group[self.max_freq].pop()
        self.freq[x] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
