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



'''
heapq 
按优先级字段排序
1、每个数字的出现频率最重要
2、出现的顺序 order, 标号
3、要记录这个数字

Runtime: 446 ms, faster than 41.89% of Python3 online submissions for Maximum Frequency Stack.
Memory Usage: 22.8 MB, less than 28.48% of Python3 online submissions for Maximum Frequency Stack.
'''
class FreqStack:

    def __init__(self):
        # val -> cnt
        self.freq = defaultdict(int)
        # heapq  (-freq_cnt, -no_th, val)
        self.h = []
        # order, no_th
        self.no = 0
        
    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.no += 1
        heappush(self.h, (-self.freq[val], -self.no, val))

    def pop(self) -> int:
        _, _, v = heappop(self.h)
        self.freq[v] -= 1
        return v
        
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()


