'''
ref: Ian
https://leetcode.cn/problems/online-majority-element-in-subarray/comments/
类似块状数组
满足时间的一种比较易懂的方法，类似块状数组的思想：
    提前记录所有频数 >=100 的数，并保存其在数组中出现位置的列表
    query 时，假如 threshold<=100，区间长度<=200，暴力枚举即可
    否则，遍历所有频数>=100 的数，并在对应的下标列表中二分查找区间的边界，即可得到该数在区间内出现的次数，与 threshold 比较即可
    数组长度最多 2 * 10^4，频数>=100的数最多200个。因此每次 query 时间最多 O(200 logN)。

执行用时：388 ms, 在所有 Python3 提交中击败了80.90% 的用户
内存消耗：26.3 MB, 在所有 Python3 提交中击败了66.29% 的用户
通过测试用例：32 / 32
'''
class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.d = defaultdict(list)
        for i, x in enumerate(arr):
            self.d[x].append(i)
        self.cand = [x for x in self.d if len(self.d[x]) > 100]
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        if threshold <= 100:
            ct = Counter(self.arr[i] for i in range(left, right + 1))
            x, w = ct.most_common(1)[0]
            return x if w >= threshold else -1
        for x in self.cand:
            w = bisect_right(self.d[x], right) - bisect_left(self.d[x], left)
            if w >= threshold:
                return x 
        return -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)


'''
ref:
https://leetcode.cn/problems/online-majority-element-in-subarray/solution/fen-xi-yi-xia-by-v5qyy4q65w-6lcx/
随机25次

执行用时：1188 ms, 在所有 Python3 提交中击败了50.56% 的用户
内存消耗：26.1 MB, 在所有 Python3 提交中击败了85.39% 的用户
通过测试用例：32 / 32
'''
class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.t = defaultdict(list)
        for i, x in enumerate(arr):
            self.t[x].append(i)
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(25):
            x = self.arr[random.randint(left, right)]
            l = bisect_left(self.t[x], left)
            r = bisect_right(self.t[x], right)
            if r - l >= threshold:
                return x
        return -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)


'''
随机20次

执行用时：920 ms, 在所有 Python3 提交中击败了65.17% 的用户
内存消耗：26.3 MB, 在所有 Python3 提交中击败了70.79% 的用户
通过测试用例：32 / 32
'''
class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.t = defaultdict(list)
        for i, x in enumerate(arr):
            self.t[x].append(i)
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20):
            x = self.arr[random.randint(left, right)]
            l = bisect_left(self.t[x], left)
            r = bisect_right(self.t[x], right)
            if r - l >= threshold:
                return x
        return -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
