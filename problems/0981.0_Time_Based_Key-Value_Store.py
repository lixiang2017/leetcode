'''
hash table + binary search

Runtime: 1502 ms, faster than 40.92% of Python3 online submissions for Time Based Key-Value Store.
Memory Usage: 70 MB, less than 90.76% of Python3 online submissions for Time Based Key-Value Store.
'''
class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not self.d[key]:
            return ''
        idx = bisect_left(self.d[key], [timestamp + 1, '']) - 1
        if idx == -1:
            return ''
        elif idx == len(self.d[key]):
            return self.d[key][-1][1]
        else:
            return self.d[key][idx][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
