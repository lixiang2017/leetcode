'''
执行用时：148 ms, 在所有 Python3 提交中击败了7.66% 的用户
内存消耗：22.7 MB, 在所有 Python3 提交中击败了16.66% 的用户
通过测试用例：30 / 30
'''
class TripleInOne:

    def __init__(self, stackSize: int):
        self.size = stackSize
        self.arr = [0] * 3 * (stackSize + 1)
        self.ptr = [0, stackSize, 2 * stackSize]
    
    def isFull(self, stackNum: int) -> bool:
        return self.ptr[stackNum] == (stackNum + 1) * self.size 

    def push(self, stackNum: int, value: int) -> None:
        if self.isFull(stackNum):
            return 
        self.ptr[stackNum] += 1
        self.arr[self.ptr[stackNum]] = value

    def pop(self, stackNum: int) -> int:
        if self.isEmpty(stackNum):
            return -1
        x = self.arr[self.ptr[stackNum]]
        self.ptr[stackNum] -= 1
        return x 

    def peek(self, stackNum: int) -> int:
        if self.isEmpty(stackNum):
            return -1        
        return self.arr[self.ptr[stackNum]]

    def isEmpty(self, stackNum: int) -> bool:
        return self.ptr[stackNum] == stackNum * self.size


# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)
