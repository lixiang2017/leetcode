'''
150 / 150 个通过测试用例
状态：通过
执行用时: 952 ms
内存消耗: 16.4 MB
提交时间：31 分钟前
'''
class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.parent[0] = -1
        # num -> user
        self.lock_memo = dict()
        self.child = defaultdict(list)
        for i, p in enumerate(parent):
            self.child[p].append(i)

    def lock(self, num: int, user: int) -> bool:
        if num in self.lock_memo:
            return False
        self.lock_memo[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if num not in self.lock_memo:
            return False
        if self.lock_memo[num] != user:
            return False
        self.lock_memo.pop(num)
        return True

    def upgrade(self, num: int, user: int) -> bool:
        # 1
        if num in self.lock_memo:
            return False
        # 2
        isChildLock = False
        q = deque(list(self.child[num]))
        while q:
            node = q.popleft()
            # print(node)
            if node in self.lock_memo:
                isChildLock = True
                break
            for ch in self.child[node]:
                q.append(ch)
        if not isChildLock:
            return False
        # 3
        p = self.parent[num]
        while p != -1:
            if p in self.lock_memo:
                return False
            else:
                p = self.parent[p]

        # upgrade
        self.lock_memo[num] = user
        q = deque(list(self.child[num]))
        while q:
            node = q.popleft()
            if node in self.lock_memo:
                self.lock_memo.pop(node)
            for ch in self.child[node]:
                q.append(ch)
        return True

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
