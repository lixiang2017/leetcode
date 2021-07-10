'''
46 / 46 个通过测试用例
状态：超出时间限制
提交时间：1 分钟内
'''
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time:
            return ''
        
        for v, t in self.time[key][:: -1]:
            if t <= timestamp:
                return v
        return ''



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


'''
执行用时：384 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：72 MB, 在所有 Python3 提交中击败了6.12% 的用户
'''
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time:
            return ''
        
        for i in range(len(self.time[key]) - 1, -1, -1):
            v, t = self.time[key][i]
            if t <= timestamp:
                return v
        return ''



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

