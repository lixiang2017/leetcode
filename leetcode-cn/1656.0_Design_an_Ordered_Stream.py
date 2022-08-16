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



'''
List / Array
T: O(N)
S: O(N)

执行用时：160 ms, 在所有 Python3 提交中击败了16.15% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了50.31% 的用户
通过测试用例：101 / 101
'''
class OrderedStream:

    def __init__(self, n: int):
        self.stream = [''] * n
        self.ptr = 0
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value 
        start = self.ptr
        while self.ptr < self.n and self.stream[self.ptr]:
            self.ptr += 1
        return self.stream[start: self.ptr] 


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)


'''
hash table

执行用时：144 ms, 在所有 Python3 提交中击败了29.19% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了80.12% 的用户
通过测试用例：101 / 101
'''
class OrderedStream:

    def __init__(self, n: int):
        self.stream = dict()
        self.ptr = 0
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value 
        start = self.ptr
        chunk = []
        while self.ptr < self.n and self.ptr in self.stream:
            chunk.append(self.stream[self.ptr])
            self.ptr += 1
        return chunk 


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)



