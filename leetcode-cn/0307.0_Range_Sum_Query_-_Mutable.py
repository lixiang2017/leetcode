'''
zkw segment tree, 张昆伟线段树


执行用时：916 ms, 在所有 Python3 提交中击败了89.64% 的用户
内存消耗：30.4 MB, 在所有 Python3 提交中击败了66.67% 的用户
通过测试用例：15 / 15
'''
class SegmentTree:
    # zkw segment tree, 张昆伟线段树
    def __init__(self, nums: List[int]):
        self.n = n = len(nums)
        self.st = [0] * 2 * n 
        # put actual nums in rear part of st
        for i in range(n, 2 * n):
            self.st[i] = nums[i - n]   # leaves
        for i in range(n - 1, -1, -1):
            self.st[i] = self.st[2 * i] + self.st[2 * i + 1]  # parent = left + right

    def update(self, i: int, val: int) -> None:
        diff = val - self.st[i + self.n]
        i += self.n 
        while i > 0:
            self.st[i] += diff 
            i //= 2

    def sumRange(self, left: int, right: int) -> int:
        s = 0
        left, right = left + self.n, right + self.n 
        while left <= right:
            if left % 2 == 1:
                s += self.st[left]
                left += 1
            if right % 2 == 0:
                s += self.st[right]
                right -= 1
            left //= 2
            right //= 2
        return s 

class NumArray:

    def __init__(self, nums: List[int]):
        self.st = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.st.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.st.sumRange(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


