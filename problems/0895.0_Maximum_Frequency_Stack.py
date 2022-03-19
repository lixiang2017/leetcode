'''
group of stacks

Runtime: 292 ms, faster than 97.19% of Python3 online submissions for Maximum Frequency Stack.
Memory Usage: 22.8 MB, less than 28.48% of Python3 online submissions for Maximum Frequency Stack.
'''
class FreqStack:

    def __init__(self):
        # val -> cnt
        self.freq = defaultdict(int)
        # 1 -> stack, 2 -> stack, 3 -> stack, ... cnt -> stack
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        # T: O(1)
        self.freq[val] += 1
        self.group[self.freq[val]].append(val)
        if self.freq[val] > self.max_freq:
            self.max_freq = self.freq[val]

    def pop(self) -> int:
        # T: O(1)
        x = self.group[self.max_freq].pop()
        self.freq[x] -= 1
        if len(self.group[self.max_freq]) == 0:
            self.max_freq -= 1
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
