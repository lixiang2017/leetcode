'''
approach: Frequency Stack
Time: push: O(1); pop: O(1)
Space: O(N), where N is the number of elements in the FreqStack.

You are here!
Your runtime beats 88.30 % of python submissions.
You are here!
Your memory usage beats 87.72 % of python submissions.
'''


class FreqStack(object):

    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.maxFreq = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.freq[x] += 1
        if self.freq[x] > self.maxFreq:
            self.maxFreq = self.freq[x]
        self.group[self.freq[x]].append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        item = self.group[self.maxFreq].pop()
        self.freq[item] -= 1
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1

        return item


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()

