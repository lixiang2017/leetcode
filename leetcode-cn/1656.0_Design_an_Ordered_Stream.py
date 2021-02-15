'''

执行结果：
通过
显示详情
执行用时：600 ms, 在所有 Python 提交中击败了36.55%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了7.04%的用户
'''


class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.ptr = 0
        self.size = n
        self.stream = [-1 for _ in range(n)]


    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.stream[idKey - 1] = value
        if self.ptr != idKey - 1 or self.ptr >= self.size:
            return []

        current_stream = []        
        while self.ptr < self.size and self.stream[self.ptr] != -1:
            current_stream.append(self.stream[self.ptr])
            self.ptr += 1
        return current_stream



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
