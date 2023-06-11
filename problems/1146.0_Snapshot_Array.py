'''
hash table + hash table

Runtime: 8025 ms, faster than 5.05% of Python3 online submissions for Snapshot Array.
Memory Usage: 40.2 MB, less than 88.69% of Python3 online submissions for Snapshot Array.
'''
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        # snap_id -> index -> val
        self.memo = defaultdict(dict)

    def set(self, index: int, val: int) -> None:
        self.memo[self.snap_id][index] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        for _id in range(snap_id, -1, -1):
            if index in self.memo[_id]:
                return self.memo[_id][index]
        return 0

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)



'''
bisect_left

Runtime: 589 ms, faster than 95.23% of Python3 online submissions for Snapshot Array.
Memory Usage: 41.1 MB, less than 77.11% of Python3 online submissions for Snapshot Array.
'''
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        # index -> [(snap_id, val), ...] pairs
        self.memo = defaultdict(list)

    def set(self, index: int, val: int) -> None:
        self.memo[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        pairs = self.memo[index]
        idx = bisect_left(pairs, [snap_id + 1, -1]) - 1
        if idx < 0:
            return 0
        else:
            return pairs[idx][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


'''
bisect_left

Runtime: 619 ms, faster than 90.19% of Python3 online submissions for Snapshot Array.
Memory Usage: 40.9 MB, less than 80.25% of Python3 online submissions for Snapshot Array.
'''
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        # index -> [(snap_id, val), ...] pairs
        self.memo = defaultdict(list)

    def set(self, index: int, val: int) -> None:
        self.memo[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        pairs = self.memo[index]
        idx = bisect_left(pairs, [snap_id, inf]) - 1
        if idx < 0:
            return 0
        else:
            return pairs[idx][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


'''
bisect_right

Runtime: 622 ms, faster than 89.10% of Python3 online submissions for Snapshot Array.
Memory Usage: 41 MB, less than 78.75% of Python3 online submissions for Snapshot Array.
'''
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        # index -> [(snap_id, val), ...] pairs
        self.memo = defaultdict(list)

    def set(self, index: int, val: int) -> None:
        self.memo[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        pairs = self.memo[index]
        idx = bisect_right(pairs, [snap_id + 1, -1]) - 1
        if idx < 0:
            return 0
        else:
            return pairs[idx][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)



'''
bisect_right

Runtime: 619 ms, faster than 90.19% of Python3 online submissions for Snapshot Array.
Memory Usage: 41.1 MB, less than 78.75% of Python3 online submissions for Snapshot Array.
'''
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        # index -> [(snap_id, val), ...] pairs
        self.memo = defaultdict(list)

    def set(self, index: int, val: int) -> None:
        self.memo[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        pairs = self.memo[index]
        idx = bisect_right(pairs, [snap_id, inf]) - 1
        if idx < 0:
            return 0
        else:
            return pairs[idx][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
